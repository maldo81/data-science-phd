# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Vision: Integrated Health & Nutrition Companion App**

This is not just a health app — it's a personal health companion that learns from each user, adapts in real time, and connects the dots between data, diet, and daily life.

### Core Concept

The application provides a unified platform where users can:
- **Monitor all health data** at a glance (vitals, labs, medications, trends)
- **Get personalized nutrition advice** tailored to their health conditions, culture, budget, and preferences
- **Receive real-time support** for eating, cooking, and living healthier
- **Learn and adapt** from how their body responds to different foods and lifestyle choices

### Current Implementation

This Django/Wagtail application currently focuses on chronic disease management (diabetes, hypertension) through:
- **Health Monitoring Dashboard**: Vitals tracking (glucose, BP, heart rate), lab results, medication management
- **AI-Powered Meal Planning**: Personalized recipes and weekly menus based on health conditions, cultural preferences, and budget
- **Smart Learning Loop**: Uses CGM data and health metrics to learn what foods work for each individual
- **Medical Device Integration**: Dexcom CGM, wearables, and Epic FHIR for comprehensive health data
- **Conversational AI**: Chat-based assistant using OpenAI/LangChain for real-time guidance
- **Real-time Updates**: Django Channels WebSocket support for live notifications

### Design Principles

When developing features, keep in mind:

1. **Personalization Through Learning**: The app learns from user preferences AND physiological responses (e.g., CGM shows glucose spike → suggest alternatives)
2. **Cultural & Budget Sensitivity**: Meal plans must respect cultural food preferences (e.g., Caribbean cuisine) and household budget constraints
3. **Holistic Health View**: Connect nutrition choices to health outcomes (blood pressure trends, glucose patterns, sleep quality)
4. **Accessibility**: Multi-language support (English/Spanish), simple dashboard design, conversational interfaces
5. **Family & Community**: Consider household needs (family of four vs. single person), shared shopping lists, multi-condition households
6. **Proactive Care**: Flag health risks early, send alerts, provide actionable recommendations before emergencies occur

### Future Extensions (Roadmap Context)

- **Family Mode**: Shared meal planning for households with diverse health needs (kids, elderly, multi-condition)
- **Clinician Dashboard**: Secure provider access to review patient data and adjust care plans
- **Public Health Analytics**: Anonymized insights for Ministry of Health on population dietary patterns and intervention impact
- **Local Economy Integration**: Connect with local grocers/farmers' markets for nearby healthy options
- **Gamification**: Health goal achievements, friendly challenges, social engagement
- **Wearables Expansion**: Integration with smartwatches, fitness trackers, sleep monitors beyond CGM

## Development Commands

### Important Note on Shell Access

**SSH Connection Issue**: This server is accessed via IP address instead of a domain name. When connecting via SSH, an interactive prompt appears that prevents automated bash commands from executing. Therefore:

- **DO NOT use the Bash tool with `python manage.py shell -c "..."` commands** - These will fail due to the SSH prompt
- **Alternative approaches**:
  - Use Django management commands directly (without shell -c)
  - Create dedicated management commands for data inspection tasks
  - Use the Django admin interface at `/health-admin/` for data exploration
  - Use direct Python scripts that import Django settings

### Running the Application
```bash
# Development server
python manage.py runserver

# WebSocket worker (Channels)
python manage.py runworker

# With specific settings module
DJANGO_SETTINGS_MODULE=healthapp.settings.dev python manage.py runserver

# Realtime worker (required for workspace queue updates)
python manage.py runworker
```

### Database Operations
```bash
# Run migrations
python manage.py migrate

# Create new migration
python manage.py makemigrations

# Create superuser
python manage.py createsuperuser
```

### Data Management
```bash
# Seed data for development
python manage.py seed_profiles
python manage.py seed_meds
python manage.py seed_cgm
python manage.py seed_meals_labs

# Ingest USDA FDC food data
python manage.py ingest_fdc data/fdc_sample.csv

# Ingest glycemic index data
python manage.py ingest_gi data/gi_data.csv

# Ingest recipes (supports CSV or JSON)
python manage.py ingest_recipes data/sample_recipes.csv --user user@example.com

# Sync external data sources
python manage.py sync_dexcom --user-id <id>
python manage.py sync_epic --user-id <id>

# Document ingestion
python manage.py ingest_doc_demo --user-id <id> --path /path/to/document.pdf
```

### Background Tasks (Celery)
```bash
# Start Celery worker (requires Redis)
celery -A healthapp worker --loglevel=info

# Start worker for specific queue
celery -A healthapp worker -Q embeddings --loglevel=info
celery -A healthapp worker -Q docs --loglevel=info
celery -A healthapp worker -Q summaries --loglevel=info

# Start Celery beat scheduler
celery -A healthapp beat --loglevel=info
```

### Static Files
```bash
# Collect static files for production
python manage.py collectstatic --noinput
```

## Architecture

### Application Structure

The project follows Django's multi-app architecture with a monorepo layout:

- **`healthapp/`** - Django project configuration
  - `settings/` - Split settings (base.py, dev.py, prod.py)
  - `urls.py` - Root URL configuration with i18n patterns
  - `routing.py` - ASGI/Channels routing for WebSockets
  - `celery.py` - Celery task queue configuration

- **`apps/healthassistant/`** - Main health assistant application
  - `data/` - Django models and migrations (separate app: `healthassistant.data`)
  - `views/` - HTTP views organized by feature (dashboard, meds, vitals, labs, foods, assistant, etc.)
  - `services/` - Business logic layer (data access, external APIs, embeddings, meal planning)
  - `core/` - AI/LLM integration (workflows, prompts, providers, tools)
  - `realtime/` - WebSocket consumers and broadcasters
  - `management/commands/` - Django management commands
  - `devices/` - Device integration (Dexcom CGM)
  - `analytics/` - Metrics and analytics

- **`apps/sitepages/`** - Wagtail CMS for marketing pages

### Key Data Models

Located in [apps/healthassistant/data/models.py](apps/healthassistant/data/models.py):

- **User & Profile**: `UserProfile`, `PatientDemographics`
  - `UserProfile` stores personalization data critical to the app's learning:
    - `conditions` (JSON) - health conditions (e.g., diabetes, hypertension)
    - `allergies` (JSON) - food allergies and intolerances
    - `dislikes` (JSON) - food preferences/dislikes
    - `cuisines` (JSON) - preferred cuisines (e.g., Caribbean, Mediterranean)
    - `budget_week` - weekly grocery budget
    - `household_size` - family composition for meal planning
    - `country`, `language` - localization preferences
  - These fields drive personalized meal recommendations, recipe filtering, and smart substitutions

- **Clinical Data**: `Medication`, `MedicationIntake`, `VitalsEntry`, `Observation`, `GlucoseReading`, `Condition`, `DeviceAccount`
  - Health data used to track patterns and correlate with nutrition choices
  - CGM readings (`GlucoseReading`) are key to learning which foods cause spikes

- **Food & Nutrition**: `FoodItem`, `FoodPortion`, `FoodGI`, `FDCFood*` (USDA FDC models in [models_fdc.py](apps/healthassistant/data/models_fdc.py))
  - Glycemic Index (GI) data stored in `FoodGI` for glucose impact predictions

- **Meal Planning**: `Recipe`, `RecipeIngredient`, `Meal`, `MealPlan`, `ShoppingList`, `ShoppingItem`, `SubstitutionRule`
  - Meals support **multi-component structure** via `components` JSON field (see [docs/meal_plan_components.md](docs/meal_plan_components.md))
  - `SubstitutionRule` enables smart food swaps based on health constraints

- **AI/Chat**: `ChatMessage`, `ChatSummary`, `ChatEmbedding` (pgvector), `Document`, `DocExtraction`
  - Conversational memory for contextual assistance ("You asked about this recipe last week...")

### Service Layer Architecture

The `apps/healthassistant/services/` directory contains business logic separated from views:

- **`week_plans.py`** - Meal plan creation, modification, and persistence
- **`recipes_ingest.py`** - Recipe normalization and auto-linking to USDA FDC foods
- **`fdc.py`** - USDA FoodData Central integration
- **`substitutions.py`** - Recipe swap suggestions based on constraints
- **`embeddings.py`** - OpenAI embeddings for semantic search
- **`retrieval.py`** - RAG (Retrieval-Augmented Generation) for chat context
- **`messages.py`** - Chat message persistence and threading
- **`document_ingest.py`** - PDF/document processing with OCR (pytesseract)
- **`epic_normalize.py`** - FHIR resource normalization from Epic
- **`users.py`**, **`context.py`**, **`provenance.py`** - Utility services

### AI/LLM Integration

The `apps/healthassistant/core/` directory handles AI-powered features:

- **Workflows** ([core/workflows/](apps/healthassistant/core/workflows/)):
  - `planning.py` - Meal plan generation workflow
  - `insights.py` - Health insights generation
- **Prompts** ([core/prompts/system.py](apps/healthassistant/core/prompts/system.py)) - System prompts for chat
- **Providers** ([core/provider/openai.py](apps/healthassistant/core/provider/openai.py)) - OpenAI API integration
- **Tools** ([core/tools/](apps/healthassistant/core/tools/)) - Function calling tools for LLM

### Real-time Features (Django Channels)

WebSocket support via [apps/healthassistant/realtime/](apps/healthassistant/realtime/):

- **Routing**: WebSocket endpoint at `ws/user/` ([routing.py](apps/healthassistant/realtime/routing.py))
- **Consumers**: `UserConsumer` handles user-specific events
- **Broadcaster**: Server-to-client notifications (plan updates, shopping lists, errors)
- **Events**: See [docs/contracts_food_phase1.md](docs/contracts_food_phase1.md) for socket event contracts

### URL Patterns

- **App routes**: `/app/*` (localized with i18n_patterns, Spanish = `/app/*`, English = `/en/app/*`)
- **Public routes**: Localized with i18n_patterns (marketing pages via Wagtail)
- **Admin**: `/health-admin/` (Django admin), `/cms/` (Wagtail CMS)
- **Auth**: `/account/login/`, `/account/signup/`, `/account/logout/`
- **Onboarding**: `/onboarding/*`

Main app URLs defined in [apps/healthassistant/urls.py](apps/healthassistant/urls.py).

### Settings Management

Settings are split across [healthapp/settings/](healthapp/settings/):
- `base.py` - Common settings (used by default via manage.py)
- `dev.py` - Development overrides
- `prod.py` - Production overrides

Environment variables loaded from `.env` file via python-dotenv. Key variables:
- `DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS`
- `PG_DB`, `PG_USER`, `PG_PASS`, `PG_HOST`, `PG_PORT` (PostgreSQL)
- `OPENAI_API_KEY`, `OPENAI_MODEL`, `EMBEDDING_MODEL`
- `DEXCOM_CLIENT_ID`, `DEXCOM_CLIENT_SECRET`, etc.
- `EPIC_CLIENT_ID`, `EPIC_FHIR_BASE`, etc.

## User Onboarding & Personalization

The app builds a comprehensive personal profile during onboarding (see `/onboarding/*` routes):

### Initial Setup Captured
- **Health Conditions**: Chronic diseases (diabetes, hypertension, etc.)
- **Allergies & Intolerances**: Foods to avoid (peanuts, dairy, etc.)
- **Food Preferences**: Likes/dislikes, preferred cuisines (e.g., "I love Caribbean food but don't like seafood")
- **Budget**: Weekly grocery spending (e.g., "$100/week")
- **Household Composition**: Single person vs. family of four, special needs (kids, elderly)
- **Cultural Context**: Language, country, regional food availability

### The Learning Loop

The app doesn't just remember preferences—it learns from physiological responses:

1. **Pattern Detection**: Machine learning analyzes correlations between:
   - Foods consumed (from meal plans) ↔ Glucose responses (from CGM)
   - Meal composition ↔ Blood pressure trends
   - Timing/portions ↔ Sleep quality, activity levels

2. **Adaptive Recommendations**:
   - If CGM shows mashed potatoes spike glucose → suggest taro root or cauliflower mash instead
   - If blood pressure rises after high-sodium meals → flag sodium contributors in recipes
   - If sleep worsens on high-caffeine days → recommend timing changes or substitutions

3. **Personal Health Fingerprint**: Over time, each user gets unique insights:
   - "Your glucose tends to spike after lunch on weekdays" (analytics module)
   - "Rice dishes work better for you with added fiber" (substitution engine)
   - "Your body responds well to split meals vs. large dinners" (pattern recognition)

### Implementation Notes
- Profile data in `UserProfile` model drives initial filtering
- `analytics/metrics.py` handles pattern detection and trend analysis
- `services/substitutions.py` uses health constraints + learned patterns for smart swaps
- `core/workflows/insights.py` generates personalized health insights from data

## Meal Planning & Recipe Ingestion

The application supports **multi-component meals** where a single meal slot (breakfast/lunch/dinner/snack) can contain multiple recipes:

### Data Flow
1. **Chat/API Input**: LLM or user provides meal plan with `components` list per slot
2. **Normalization**: `services.recipes_ingest.ingest_recipes()` processes components
3. **Auto-linking**: Ingredients are automatically matched to USDA FDC foods when `auto_link_fdc=True`
4. **Persistence**: `services.week_plans.save_plan()` stores meals with component structure
5. **Shopping Lists**: Automatically generated from all component recipes

### Conversational Assistant Features

The AI assistant (accessible at `/app/assistant/` in Spanish, `/en/app/assistant/` in English) provides real-time support for:

1. **What-If Planning**: Natural language queries like:
   - "Can you make me a 3-day menu under 1,200 calories a day, low sodium, and within $80?"
   - "What happens if I swap rice for quinoa in this recipe?"
   - "Show me Caribbean breakfast options under 50g carbs"

2. **Cooking Companion**: Step-by-step guidance:
   - "Now sauté the onions... want me to time this for 5 minutes?"
   - "What's the next step?" → Contextual recipe instructions
   - "How do I know when it's done?" → Visual/texture cues

3. **Health Context Integration**:
   - "Your blood sugar is steady this morning, here are some breakfast options"
   - "I notice your BP has been high after salty meals—let's try this low-sodium version"
   - Uses RAG (Retrieval-Augmented Generation) to pull relevant health history

4. **Adaptive Suggestions**:
   - Learns from past conversations (via `ChatEmbedding` vector search)
   - References uploaded documents (medical records, diet plans via `Document` model)
   - Personalizes based on profile + recent health trends

### Chat Response Contract

The assistant returns structured JSON envelopes. See [docs/contracts_food_phase1.md](docs/contracts_food_phase1.md) for:
- `plan_preview` payload format
- `shopping_list` payload format
- `nutrition` breakdown (meal/day/week scope)
- `swap_suggestion` payload for recipe substitutions
- WebSocket event schemas

Key points:
- Meals have a `components` JSON field containing ordered list of recipes
- First component becomes primary `recipe_id` for backward compatibility
- Nutrition aggregates across all components
- Shopping lists iterate over all component recipes
- Real-time updates pushed via WebSocket to `ws/user/` (plan.created, plan.updated, shopping_list.updated events)

## Background Tasks (Celery)

Task queues defined in [healthapp/settings/base.py](healthapp/settings/base.py:240-263):
- `embeddings` - Text embedding generation (OpenAI API)
- `docs` - Document ingestion and extraction
- `summaries` - Chat summary rollup (runs hourly via Celery Beat)

Tasks defined in [apps/healthassistant/tasks.py](apps/healthassistant/tasks.py):
- `embed_texts_task` - Embed text chunks for semantic search
- `embed_chatmessages_task` - Embed chat messages
- `rollup_chat_summary_task` - Generate conversation summaries
- `docs_ingest_task` - Process uploaded documents (PDF extraction, OCR)

## Database & Migrations

- **Primary DB**: PostgreSQL with pgvector extension for embeddings
- **Fallback**: SQLite for local development (configured in settings)
- **Vector Search**: Uses pgvector for cosine similarity searches on 3072-dim embeddings
- **Extensions**: Migration 0014 enables pgvector, 0019 enables pg_trgm for fuzzy text search

## External Integrations

### Dexcom CGM
- OAuth flow for device authorization
- Sync command: `python manage.py sync_dexcom --user-id <id>`
- Models: `DeviceAccount`, `GlucoseReading`
- Service: [apps/healthassistant/devices/dexcom.py](apps/healthassistant/devices/dexcom.py)

### Epic FHIR
- OAuth flow for EHR access
- Sync command: `python manage.py sync_epic --user-id <id>`
- Normalizes FHIR resources (Patient, Condition, Observation, MedicationStatement)
- Service: [apps/healthassistant/services/epic_normalize.py](apps/healthassistant/services/epic_normalize.py)

### USDA FoodData Central
- Local subset of FDC database stored in `FDCFood*` models
- Ingredient auto-linking via fuzzy string matching
- Ingest command: `python manage.py ingest_fdc`

## Development Philosophy

When building features for this application, always consider the broader vision:

### User-Centric Design
- **Empowerment over Prescription**: Help users understand and control their health, don't just tell them what to do
- **Cultural Sensitivity**: Food is deeply cultural—respect regional cuisines, cooking methods, and ingredient availability
- **Accessibility First**: Assume users have varying literacy levels, technical skills, and language preferences
- **Trust Through Transparency**: Show why recommendations are made, source of data, confidence levels

### Data-Driven Personalization
- **Observe First, Recommend Second**: Collect health data patterns before making suggestions
- **Fail Gracefully**: If CGM disconnects or data is incomplete, provide sensible defaults based on profile
- **Privacy by Design**: Health data is sensitive—always consider data minimization and user consent
- **Multi-Modal Learning**: Combine explicit preferences (user says "I don't like fish") with implicit signals (CGM shows spike after rice)

### Scalability Considerations
- **Family → Community → Population**: Features should scale from individual to household to public health
- **Provider Integration**: Design with clinician workflows in mind (future dashboard for doctors/nutritionists)
- **Local Economy**: Consider how to connect users with local food sources (markets, grocers, farms)
- **International Expansion**: Architecture should support different food databases, health systems, and regulations

### Key Stakeholder Value
- **For Users**: Daily support, knowledge, control over health decisions
- **For Providers**: Better patient data, early intervention signals, reduced ER visits
- **For Public Health**: Population-level insights into chronic disease patterns (diabetes, hypertension)
- **For Investors**: Scalable SaaS model with B2C and B2B2C (through health systems) opportunities

## Important Notes

### Import Paths
- Apps are in `sys.path` via `settings/base.py:8`, so use `from healthassistant.X import Y` not `from apps.healthassistant.X import Y`
- Exception: URL includes use full module path like `"healthassistant.urls"`

### Multi-language Support
- Wagtail i18n enabled with English/Spanish
- Locale files in `locale/` directory
- Public routes use `i18n_patterns` with `prefix_default_language=False`
- App routes (`/app/*`) are non-localized for stable bookmarks

### File Storage
- Documents stored in `/var/app_data/insights_docs` (configurable via `DOCS_STORAGE_ROOT`)
- Static files served via WhiteNoise
- Media files in `media/` directory

### Embeddings
- Controlled by `EMBEDDINGS_ENABLED` environment variable
- Uses OpenAI `text-embedding-3-large` (3072 dimensions)
- Stored in `ChatEmbedding` model with pgvector index
- Used for RAG in chat assistant

### Code to Delete
Files marked `*_to_delete.py` are deprecated and pending removal:
- `services/data_access_to_delete.py`
- `views/forms_to_delete.py`
- `views/pages_to_delete.py`
