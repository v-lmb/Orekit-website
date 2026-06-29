# Load Testing

## Tool
[Locust](https://locust.io) open-source load testing framework in Python

## Installation

```bash
pip install locust
```

Running the tests
Start the API and database first (see RUNBOOK §3), then :
```bash
locust -f apps/api/tests/locustfile.py
```

Open the Locust web UI at http://localhost:8089, set the number of users and spawn rate, then start.

## Test scenarios

File: `apps/api/tests/locustfile.py`

| Task | Endpoint | Weight | Purptose |
|--------|---------|------| ---------- |
| health | `GET /health` | 1 | Baseline, DB ping latency |
| get_all_tle | `GET /api/tle` | 3 | Most expensive query, full table scan |
| get_tle_by_id | `GET /api/tle/25544` | 3 | Indexed lookup (ISS) |
| get_tle_not_found | `GET /api/tle/99999999999` | 1 | Error handling under load |

Wait time between requests: 1-3 seconds per simulated user.


## Interpreting results

- RPS (requests/second): target > 3.7 req/s to match or exceed the current site
- p95 response time: should stay under 500 ms under normal load
- Failure rate: should be 0% (excluding intentional 404s)

## Results

Test run 3 : 2026-06-26 > 10 simulated users, spawn rate 2/s, 2 minutes.

| Endpoint | Requests | Failures | Median (ms) | p95 (ms) | RPS |
|----------|----------|----------|-------------|----------|-----|
| `GET /api/tle` | 258 | 0 | 7 | 11 | 2.1 |
| `GET /api/tle/25544` | 204 | 0 | 4 | 7 | 1.8 |
| `GET /api/tle/99999999999` | 59 | 0 | 4 | 6 | 0.6 |
| `GET /health` | 87 | 0 | 3 | 6 | 0.5 |
| **Aggregated** | **608** | **0** | **6** | **10** | **5.0** |

**Conclusion:** 0 failures. 5.0 RPS aggregate.

`GET /api/tle` drops to a median of 7 ms with pagination enabled (limit=100, ~29 KB response).\
Runs 1 and 2 were performed using an outdated Docker image without pagination and do not constitute a valid baseline.

## Rate limiting verification

**Tool :** curl (manual test)\
**Date :** 2026-06-29

**Command:**
```bash
for i in $(seq 1 65); do curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8001/api/tle; done
```

**Result :**\
60 × `200 OK` then 5 × `429 Too Many Requests`

**Conclusion :**\
Rate limit of 60 requests/minute per IP enforced correctly with slowapi
Clients exceeding the threshold receive `429 Too Many Requests`
