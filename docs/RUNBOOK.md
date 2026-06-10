# RUNBOOK

<!-- This document covers only related topics : -->
<!-- local startup, migrations, TLE ingestion and what to check in case of problem. -->
<!-- The infrastructure portion (DNS, TLS, reverse proxy, backups, monitoring) is managed by the maintainers. -->

---

## 1.Prerequisites
- Docker >= 24 and Docker Compose >= 2.20
- (optional for Alembic commands outside of Docker) Python 3.11+
- Access to project's GitHub Container Registry (`ghcr.io/org/orekit-website`)
- Git configured with read permissions for the repository

## 2.Environment variables
Copy `.env.example` to `.env` in the project root directory and fill in the actual values.

```bash
cp .env.example .env
```

| Variable | Description | Example |
|---|---|---|
| `DATABASE_URL` | Full PostgreSQL connection URL | `postgresql://orekit:changeme@db:5432/orekit` |
| `API_HOST` | Backend listening interface | `0.0.0.0` |
| `API_PORT` | Backend listening port | `8000` |
| `CORS_ALLOWED_ORIGINS` | Allowed origins, separated by commas (no wildcards) | `http://localhost:3000` |
| `TLE_FETCH_INTERVAL_HOURS` | Celestrak ingestion frequency in hours | `6` |
| `TLE_GROUPS` | Celestrak groups to ingest, separated by commas | `stations,active` |
| `TLE_FETCH_TIMEOUT_SECONDS` | Timeout per Celestrak request | `30` |
| `TLE_MAX_RETRIES` | Maximum number of retry attempts on failure | `3` |
| `CI_REGISTRY_IMAGE` | Path to the Docker image in the registry (CI only) | `ghcr.io/org/orekit-website` |

## 3.Local startup (Docker Compose)
Run all commands from the project root unless stated otherwise.

- Start the database
```bash
docker compose -f compose/docker-compose.yml up -d
```

- Activate the Python environment
```bash               
cd apps/api && source venv/bin/activate
```

- Start the API
```bash
uvicorn main:app --reload
```

To verify the API is running, open http://localhost:8001/health in your
browser or run:
```bash
curl http://localhost:8001/health
```
Expected response: `{"status": "okay"}`


## 4.Alembic migrations
Run the following commands from `apps/api/`
- If this is the first time the project is being installed
```bash
pip install -r requirements.txt
```

- Apply the Alembic migrations
```bash
alembic upgrade head
```

## 5.TLE ingestion
Run the following commands from `apps/api/`
- Fetches TLE data from Celestrak and stores it in the database
```bash
python ingest.py
```

## 6.Deployment (maintainer-side)
<!-- à compléter -->

## 7.Logs
<!-- à compléter -->

## 8.Common issues
<!-- à compléter -->
