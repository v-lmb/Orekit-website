# Data Model 

## Table `tle`

### Columns

| Column | Type | Description |
|--------|------|-------------|
| ID | INTEGER | Auto-incrementing primary key |
| satellite_id | VARCHAR(20) | NORAD satellite identifier |
| name | VARCHAR(100) | Satellite name |
| line1 | VARCHAR(69) | First TLE line |
| line2 | VARCHAR(69) | Second TLE line |
| source_group | VARCHAR(50) | Celestrak group the satellite was ingested from (e.g. stations, active) |
| ingested_at | TIMESTAMPTZ | Timestamp of last ingestion (UTC) |

### Constraints

- `UNIQUE (satellite_id, source_group)` : a satellite can appear in multiple Celestrak groups

### Example row
```
[
  {
    "id": 1,
    "satellite_id": "25544",
    "name": "ISS (ZARYA)",
    "line1": "1 25544U 98067A   26154.96745432  .00008451  00000+0  15807-3 0  9999",
    "line2": "2 25544  51.6330   5.5404 0007082 130.0270 230.1341 15.49590346569705",
    "source_group": "stations",
    "ingested_at": "2026-06-03T16:33:56.520906+00:00"
  }
]
```
