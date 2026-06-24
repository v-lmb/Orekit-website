import os
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential
from sqlalchemy.dialects.postgresql import insert
from database import SessionLocal
from models import Tle

# Celestrak endpoint, {group} is replaced at fetch time
CELESTRAK_URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP={group}&FORMAT=tle"

# groups to ingest, configurable via TLE_GROUPS env var
GROUPS = os.getenv("TLE_GROUPS", "stations,active").split(",")


# retries up to 3 times with exponential backoff (2s, 4s, 8s) on failure
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def fetch_tle(group: str) -> str:
    """Fetches raw TLE text from Celestrak for a given group"""
    headers = {"User-Agent": "orekit-website/1.0"}
    response = httpx.get(CELESTRAK_URL.format(group=group), timeout=10, headers=headers)
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
        satellite_id = line1[2:7].strip()  # NORAD ID is ta fixed posistions 2-7 in line 1
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
                }
            )
            db.execute(stmt)
        db.commit()
    finally:
        db.close()


# Run the script to test it
if __name__ == "__main__":
    ingest()
