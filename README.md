# Orekit Website - V1

![Banner](docs/assets/README_banner.png)

## Description
**Orekit is an open source astrodynamics library** developed by CS Group and maintained by a community of space engineers.\
It provides low-level components for orbital mechanics: orbit propagation, attitude computation, coordinate frame transformations, and TLE (Two-Line Element) processing. It is written in _Java_ and widely used in the space industry.

This project is a full redesign of [orekit.org](https://www.orekit.org/), built as a Holberton School portfolio project.\
It replaces the existing Jekyll static site with a modern stack: a Nuxt 3 static frontend featuring a live CesiumJS 3D satellite tracking viewer, backed by a FastAPI REST API that ingests and serves TLE orbital data from Celestrak.

---

## Project Structure

```
Orekit-website/
│
├── apps/
│   ├── api/                    # FastAPI backend
│   │   ├── main.py             # App entry point, routes, middleware
│   │   ├── models.py           # SQLAlchemy Tle model
│   │   ├── database.py         # DB session factory
│   │   ├── ingest.py           # Celestrak TLE ingestion
│   │   ├── alembic/            # Database migrations
│   │   └── tests/              # pytest + testcontainers + locust
│   └── web/                    # Nuxt 3 frontend
│       ├── app/                # App shell + components
│       └── pages/              # Vue pages (one file per route)
│
├── compose/
│   └── docker-compose.yml
│
├── docs/
│   ├── api.md                  # API reference
│   ├── data-model.md           # Database schema
│   ├── RUNBOOK.md              # Operational runbook
│   ├── security.md             # Security checklist
│   ├── openapi.json            # Archived OpenAPI spec
│   ├── load-test.md            # Load test results
│   └── sprints/                # Sprint plans, reviews, retrospectives
│
├── .env.example
└── README.md
```

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

## Technologies

| Layer | Technology |
|-------|------------|
| Frontend | ![Nuxt 3](https://img.shields.io/badge/Nuxt_3-00DC82?style=flat&logo=nuxt.js&logoColor=white) ![Vue 3](https://img.shields.io/badge/Vue_3-4FC08D?style=flat&logo=vue.js&logoColor=white) ![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat&logo=vite&logoColor=white) static generation |
| 3D viewer | ![CesiumJS](https://img.shields.io/badge/CesiumJS-6CADDF?style=flat&logo=cesium&logoColor=white) + satellite.js (SGP4) |
| Backend | ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white) ![Python](https://img.shields.io/badge/Python_3.11-3776AB?style=flat&logo=python&logoColor=white) |
| ORM | ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy_2-D71F00?style=flat&logoColor=white) + Alembic |
| Database | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL_15-4169E1?style=flat&logo=postgresql&logoColor=white) |
| HTTP client | ![httpx](https://img.shields.io/badge/httpx-000000?style=flat&logoColor=white) + tenacity |
| Scheduler | APScheduler |
| Rate limiting | slowapi |
| CI | ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white) lint → test → build |
| Registry | ![ghcr.io](https://img.shields.io/badge/ghcr.io-181717?style=flat&logo=github&logoColor=white) |
| Testing | ![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat&logo=pytest&logoColor=white) ![Locust](https://img.shields.io/badge/Locust-00B140?style=flat&logoColor=white) |

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

Rate limit :\
60 requests/minute per IP on TLE endpoints

Full OpenAPI spec :\
[`docs/openapi.json`](docs/openapi.json), interactive docs at `/docs` when the API is running

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

Reference baseline :\
5.0 RPS, p95 = 10 ms, 0 failures (10 concurrent users, 2 min)

---

## CI Pipeline

GitHub Actions runs three jobs on every push :

1. **lint** : ruff (Python)
2. **test** : pytest + testcontainers (real PostgreSQL)
3. **build** : Docker image pushed to ghcr.io

---

## Documentation

- [API reference](docs/api.md)
- [Data model](docs/data-model.md)
- [Runbook](docs/RUNBOOK.md)
- [Security checklist](docs/security.md)
- [Load test results](docs/load-test.md)

---

## Team
- [Allix Robin](https://github.com/AllixRbn) : Frontend (Nuxt 3, CesiumJS)
- [Virginie Lombarte](https://github.com/v-lmb) : Backend (FastAPI, PostgreSQL)

**Maintainer :**\
Vincent CUCCHIETTI and Orekit's community


