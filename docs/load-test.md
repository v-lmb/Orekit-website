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

Wait time between requests: 1–3 seconds per simulated user.


## Interpreting results

- RPS (requests/second): target > 3.7 req/s to match or exceed the current site
- p95 response time: should stay under 500 ms under normal load
- Failure rate: should be 0% (excluding intentional 404s)

## Results
Test run : 2026-06-18 > 10 simulated users, spawn rate 2/s, ~2 minutes.

| Endpoint | Requests | Failures | Median (ms) | p95 (ms) | RPS |
|----------|----------|----------|-------------|----------|-----|
| `GET /api/tle` | 153 | 0 | 700 | 1300 | 1.1 |
| `GET /api/tle/25544` | 173 | 0 | 56 | 720 | 1.8 |
| `GET /api/tle/99999999999` | 64 | 0 | 29 | 460 | 0.9 |
| `GET /health` | 48 | 0 | 28 | 770 | 0.5 |
| **Aggregated** | **438** | **0** | **330** | **1200** | **4.3** |

**Conclusion:** 0 failures. 4.3 RPS aggregate vs 3.7 RPS on the current orekit.org target met.

`GET /api/tle` is the slowest endpoint (700 ms median, 4.4 MB response) due to the full table scan returning all TLEs\
This is expected in v1, pagination would address it but is out of scope.
