---
name: translate-frontend
description: Run the frontend localization workflow for English/Spanish parity in this repository. Use when UI text changes and translation extraction, machine draft translation, compilation, and parity checks are needed.
---

# Translate Frontend Strings (Bilingual)

Use this workflow when user-facing UI text changes and English/Spanish parity must be maintained.

If your project is not Django-based, adapt command paths to your framework/toolchain.

## 1. Extract Django strings

```bash
.venv/bin/python manage.py makemessages -l es
```

## 2. Draft missing translations

```bash
.venv/bin/python scripts/auto_translate_openai_v2.py --po-file locale/es/LC_MESSAGES/django.po
```

If previous runs left `msgstr == msgid` entries, run:

```bash
.venv/bin/python scripts/auto_translate_openai_v2.py --po-file locale/es/LC_MESSAGES/django.po --translate-identical
```

## 3. Clear fuzzy flags

```bash
.venv/bin/python scripts/auto_translate_openai_v2.py --po-file locale/es/LC_MESSAGES/django.po --clear-fuzzy-only
```

## 4. Compile translations

```bash
.venv/bin/python manage.py compilemessages -l es
```

## 5. Enforce completeness

```bash
.venv/bin/python scripts/qa/check_translations.py --po-file locale/es/LC_MESSAGES/django.po
```

## 6. Recommended checks

Template literal detection:

```bash
.venv/bin/python scripts/qa/check_template_literals.py
```

JavaScript catalog flow:

```bash
.venv/bin/python manage.py makemessages -d djangojs -l es
.venv/bin/python scripts/auto_translate_openai_v2.py --po-file locale/es/LC_MESSAGES/djangojs.po
.venv/bin/python scripts/auto_translate_openai_v2.py --po-file locale/es/LC_MESSAGES/djangojs.po --translate-identical
.venv/bin/python scripts/qa/check_translations.py --po-file locale/es/LC_MESSAGES/djangojs.po
```

## 7. Verify in UI

Review affected pages in Spanish for quality and layout regressions.

## Notes

- Requires `OPENAI_API_KEY` and `OPENAI_MODEL`.
- Requires dependencies from `requirements.txt`.
