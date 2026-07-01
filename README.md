# Orekit Website - V1

A redesign of [orekit.org](https://www.orekit.org) built as a Holberton School portfolio project

**Team :**
- [Allix Robin](https://github.com/AllixRbn) : Frontend (Nuxt 3, CesiumJS)
- [Virginie Lombarte](https://github.com/v-lmb) : Backend (FastAPI, PostgreSQL)

**Maintainer :** Orekit community

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Browser                              │
│                      Nuxt 3 (SSG)                           │
│                CesiumJS 3D globe viewer                     │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP GET /api/tle
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                   FastAPI (Python 3.11)                     │
│                       GET /health                           │
│                      GET /api/tle                           │
│                 GET /api/tle/{satellite_id}                 │
│                         CORS                                │
│                   Security headers                          │
│				Rate limiting (60 req/min/IP)                 │
│              APScheduler - ingestion every 6hours           │                                                             
└─────────────────────┬───────────────────────────────────────┘
                      │ SQLAlchemy 2 / psycopg2
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  PostgreSQL 15                              │
│                    table: tle                               │
└─────────────────────────────────────────────────────────────┘
                      ▲
                      │ httpx + tenacity (retry)
              Celestrak TLE API
     (https://celestrak.org/NORAD/elements/gp.php)
```

All three services are orchestrated locally with **Docker Compose** (`compose/docker-compose.yml`)

---

## Database Schema

```
┌───────────────────────────────────────────────────┐
│                      tle                          │
├────────────────┬───────────────┬──────────────────┤
│    Column      │     Type      │     Notes        │
├────────────────┼───────────────┼──────────────────┤
│ id             │ INTEGER       │ PK, auto-incr    │
│ satellite_id   │ VARCHAR(20)   │ NORAD ID         │
│ name           │ VARCHAR(100)  │ Satellite name   │
│ line1          │ VARCHAR(69)   │ TLE line 1       │
│ line2          │ VARCHAR(69)   │ TLE line 2       │
│ source_group   │ VARCHAR(50)   │ Celestrak group  │
│ ingested_at    │ TIMESTAMPTZ   │ Last upsert      │
├────────────────┴───────────────┴──────────────────┤
│       UNIQUE (satellite_id, source_group)         │
└───────────────────────────────────────────────────┘
```

`ingested_at` is updated on every ingestion run it reflects the last time the record was refreshed from Celestrak, not the date of first insertion.

---

## Stack

|    Layer      |       Technology                              |
|---------------|-----------------------------------------------|
| Frontend      | Nuxt 3 (Vue 3 + Vite), static generation      |
| 3D viewer     | CesiumJS + satellite.js (SGP4)                |
| Backend       | FastAPI, Python 3.11                          |
| ORM           | SQLAlchemy 2 + Alembic                        |
| Database      | PostgreSQL 15                                 |
| HTTP client   | httpx + tenacity                              |
| Scheduler     | APScheduler                                   |
| Rate limiting | slowapi                                       |
| CI            | GitHub Actions (lint > test > build)          |
| Registry      | ghcr.io                                       |

---

## Local Development

### Prerequisites

- Docker + Docker Compose
- Python 3.11+ (for running tests or ingest manually)

### Start all services

```bash
docker compose -f compose/docker-compose.yml up -d --build
```

Services :
- Frontend : http://localhost:3000
- API : http://localhost:8000
- Swagger UI : http://localhost:8000/docs
- PostgreSQL : localhost:5433

### Apply migrations

```bash
docker compose -f compose/docker-compose.yml exec api alembic upgrade head
```

### Run TLE ingestion manually

```bash
docker compose -f compose/docker-compose.yml exec api python ingest.py
```

### Environment variables

Copy `.env.example` to `apps/api/.env` and fill in the values

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | — | PostgreSQL connection string |
| `TLE_FETCH_INTERVAL_HOURS` | `6` | Ingestion interval (hours) |
| `TLE_MAX_RETRIES` | `3` | Celestrak retry attempts |
| `TLE_RETRY_MAX_WAIT` | `10` | Max wait between retries (seconds) |
| `TLE_FETCH_TIMEOUT_SECONDS` | `30` | HTTP timeout (seconds) |
| `CORS_ALLOWED_ORIGINS` | `http://localhost:3000` | Comma separated allowed origins |

---

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Database connectivity check |
| GET | `/api/tle` | List TLEs ; params: `limit`, `offset`, `group` |
| GET | `/api/tle/{satellite_id}` | Get one satellite by NORAD ID |

Rate limit : 60 requests/minute per IP on TLE endpoints

Full OpenAPI spec : [`docs/openapi.json`](docs/openapi.json), interactive docs at `/docs` when the API is running

---

## Testing

### Unit + integration tests

Tests run against a real PostgreSQL instance spun up by testcontainers (no mocks)

```bash
cd apps/api
source venv/bin/activate
python -m pytest tests/ -v
```

9/9 tests passing and CI runs the full suite on every push to `dev`

### Load testing

```bash
pip install locust
locust -f apps/api/tests/locustfile.py --host http://localhost:8000
```

Reference baseline : 5.0 RPS, p95 = 10 ms, 0 failures (10 concurrent users, 2 min)

---

## CI Pipeline

GitHub Actions runs three jobs on every push :

1. **lint** : ruff (Python)
2. **test** : pytest + testcontainers (real PostgreSQL)
3. **build** : Docker image pushed to ghcr.io

---

## Project Structure

```
apps/
  api/            # FastAPI backend
    main.py       # App entry point, routes, middleware
    models.py     # SQLAlchemy Tle model
    database.py   # DB session factory
    ingest.py     # Celestrak TLE ingestion
    alembic/      # Database migrations
    tests/        # pytest + testcontainers + locust
  web/            # Nuxt 3 frontend
    pages/        # Vue pages
    app/          # App shell
compose/
  docker-compose.yml
docs/
  api.md          # API reference
  data-model.md   # Database schema
  RUNBOOK.md      # Operational runbook
  security.md     # Security checklist
  openapi.json    # Archived OpenAPI spec
  load-test.md    # Load test results
```

---

## Documentation

- [API reference](docs/api.md)
- [Data model](docs/data-model.md)
- [Runbook](docs/RUNBOOK.md)
- [Security checklist](docs/security.md)
- [Load test results](docs/load-test.md)
