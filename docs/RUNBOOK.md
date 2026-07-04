# RUNBOOK

<!-- This document covers only related topics : -->
<!-- local startup, migrations, TLE ingestion and what to check in case of problem. -->
<!-- The infrastructure portion (DNS, TLS, reverse proxy, backups, monitoring) is managed by the maintainers. -->

---

## 1.Prerequisites
- Docker >= 24 and Docker Compose >= 2.20
- (optional for Alembic commands outside of Docker) Python 3.11+
- Access to project's GitHub Container Registry (`ghcr.io/v-lmb/orekit-website`)
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
| `CI_REGISTRY_IMAGE` | Path to the Docker image in the registry (CI only) | `ghcr.io/v-lmb/orekit-website` |

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
browser or run
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
> This section is addressed to the maintainer.\
> Reverse proxy, TLS, DNS, backups, and hosting are out of student scope.

### 6.1 Artefacts delivered by the student team

| Artefact | Location |
|---|---|
| Backend Docker image | published by CI to ghcr.io on every merge to `main` |
| Alembic migrations | `apps/api/alembic/versions/` |
| Environment template | `.env.example` at project root |
| OpenAPI schema | `docs/openapi.json` |

### 6.2 First deployment

1. Pull the image
```bash
docker pull ghcr.io/<org>/orekit-website-api:<tag>
```

2. Copy and fill the environment file (see §2)
```bash
cp .env.example .env
```

3. Start the services
```bash
docker compose -f compose/docker-compose.yml up -d
```

4. Apply migrations
```bash
docker compose -f compose/docker-compose.yml exec api alembic upgrade head
```

5. Trigger initial TLE ingestion
```bash
docker compose -f compose/docker-compose.yml exec api python ingest.py
```

6. Verify
```bash
curl http://<host>:<port>/health
```

### 6.3 Subsequent updates

1. Pull the new image and restart
```bash
docker compose -f compose/docker-compose.yml pull
docker compose -f compose/docker-compose.yml up -d --build
```

2. Apply new migrations if any
```bash
docker compose -f compose/docker-compose.yml exec api alembic upgrade head
```

### 6.4 Reverse proxy

The API must sit behind a reverse proxy (e.g. Caddy, nginx) handling TLS termination and HSTS.\
Set `CORS_ALLOWED_ORIGINS` to the production frontend domain.

### 6.5 Backups

The tle table is repopulated automatically from Celestrak every `TLE_FETCH_INTERVAL_HOURS` hours, low risk to lose.\
Still include the PostgreSQL volume in
your backup policy.

## 7.Logs
Run all commands from the project root unless stated otherwise.\
View API logs in real time
```bash
docker compose logs -f api
```

Displays the logs for the PostgreSQL container
```bash
docker compose logs -f db
```

Options
- `-f` : monitors logs in real time
- `--tail=100` : displays the last 100 lines

## 8.Common issues
### Problem 1 : The database won't start
**Symptom :** The API returns a connection error; /health fails\
**Cause :** Docker Compose is not running\
**Solution :** Run Docker Compose from root 
```bash
docker compose -f compose/docker-compose.yml up -d
```

### Problem 2 : Celestrak 403
**Symptom :** Celestrak returns a 403 error\
**Cause :** Rate limit\
**Solution :** Wait a few minutes and try again

### Problem 3 : API crashes on startup
**Symptom :** The API crashes on startup with a `KeyError: DATABASE_URL` error\
**Cause :** .env file is missing or misconfigured\
**Solution :** Copy `.env.example` to `.env` and fill in the correct values (see §2.Environment variables)
