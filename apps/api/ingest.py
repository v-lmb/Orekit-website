import os
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential
from sqlalchemy.dialects.postgresql import insert
from database import SessionLocal
from models import Tle
import logging

logger = logging.getLogger(__name__)

# Celestrak endpoint, {group} is replaced at fetch time
CELESTRAK_URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP={group}&FORMAT=tle"

# groups to ingest, configurable via TLE_GROUPS env var
GROUPS = os.getenv("TLE_GROUPS", "stations,active").split(",")

RETRY_ATTEMPS = int(os.getenv("TLE_MAX_RETRIES", "3"))
RETRY_MAX_WAIT = int(os.getenv("TLE_RETRY_MAX_WAIT", "10"))
FETCH_TIME_OUT = int(os.getenv("TLE_FETCH_TIMEOUT_SECONDS", "10"))


# retries up to 3 times with exponential backoff (2s, 4s, 8s) on failure
@retry(stop=stop_after_attempt(RETRY_ATTEMPS), wait=wait_exponential(multiplier=1, min=2, max=RETRY_MAX_WAIT))
def fetch_tle(group: str) -> str:
    """Fetches raw TLE text from Celestrak for a given group"""
    headers = {"User-Agent": "orekit-website/1.0"}
    response = httpx.get(CELESTRAK_URL.format(group=group), timeout=FETCH_TIME_OUT, headers=headers)
    response.raise_for_status()
    return response.text


def parse_tle(text: str, group: str) -> list[dict]:
    """parses and structures the TLE data into a list of dictionaries"""
    lines = text.strip().splitlines()
    entries = []
    i = 0
    while i < len(lines) - 2:
        name = lines[i].strip()
        line1 = lines[i + 1].strip()
        line2 = lines[i + 2].strip()
        satellite_id = line1[2:7].strip()  # NORAD ID is at fixed posistions 2-7 in line 1
        entries.append({
            "satellite_id": satellite_id,
            "name": name,
            "line1": line1,
            "line2": line2,
            "source_group": group,
        })
        i += 3
    return entries


def ingest():
    """
    Opens a database session, fetches and parses TLE data for each group,
    and upserts satellites / inserting new ones or updating existing ones
    """
    db = SessionLocal()
    try:
        for group in GROUPS:
            text = fetch_tle(group)
            entries = parse_tle(text, group)
            stmt = insert(Tle).values(entries)
            stmt = stmt.on_conflict_do_update(
                index_elements=["satellite_id", "source_group"],
                set_={
                    "name": stmt.excluded.name,
                    "line1": stmt.excluded.line1,
                    "line2": stmt.excluded.line2,
                    "ingested_at": stmt.excluded.ingested_at,
                }
            )
            db.execute(stmt)
            logger.info("Ingested group '%s' : %d entries", group, len(entries))
        db.commit()
    except Exception as e:
        logger.error("Ingestion failed: %s", e)
        raise
    finally:
        db.close()


# Run the script to test it
if __name__ == "__main__":
    ingest()
