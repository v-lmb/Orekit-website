from ingest import parse_tle

"""
SAMPLE_TLE :
ISS TLE used for testing
"""
SAMPLE_TLE = """ISS (ZARYA)
1 25544U 98067A   21275.51782528  .00001977  00000-0  45623-4 0  9993
2 25544  51.6461 177.7014 0002829 317.6439 150.3229 15.48815838305102"""


def test_parse_tle_returns_one_entry():
    """
    Pass the SAMPLE_TLE block to `parse_tle`
    and verify that it returns exactly 1 entry.
    """
    result = parse_tle(SAMPLE_TLE, "stations")
    assert len(result) == 1


def test_parse_tle_fields():
    """
    Returns the same block and verifies that every field in the returned dictionary
    is correct: the name, the ID, the group, and the two lines.
    Tests that the extraction is accurate
    """
    result = parse_tle(SAMPLE_TLE, "stations")
    entry = result[0]
    assert entry["name"] == "ISS (ZARYA)"
    assert entry["satellite_id"] == "25544"
    assert entry["source_group"] == "stations"
    assert entry["line1"].startswith("1 25544")
    assert entry["line2"].startswith("2 25544")


def test_parse_tle_multiple_entries():
    """
    Provide two blocks (SAMPLE_TLE and another TLE),
    and verify that `parse_tle` returns two entries.
    Test that the `while` loop in `parse_tle` works correctly.
    """
    two_sats = SAMPLE_TLE + "\nNOAA 15\n1 25338U 98030A   21275.52567824  .00000018  00000-0  29692-409993\n2 25338  98.7193  14.7544 0010900 332.2582  27.7942 14.25859049213567"
    result = parse_tle(two_sats, "active")
    assert len(result) == 2
