#!/usr/bin/env python3
"""Optional entrypoint for future automated skill evals.

This script is intentionally manual-by-default to avoid extra API billing.
"""

import os
import sys


def main() -> int:
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("SKIPPED: no API key configured. Use scripts/qa/manual_skill_eval.md.")
        return 0

    print("Automated skill eval scaffold detected API key.")
    print("Implement provider-specific eval runner when you choose to enable paid automation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
