from models import Tle


def test_health(client):
    """
    Verify that the /health endpoint
    returns a 200 status code and {“status”: “okay”}
    Confirm that the API is running and connected to the database
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "okay"}


def test_list_tle_empty(client):
    """
    Verify that /api/tle returns an empty list
    when the database contains no satellites
    """
    response = client.get("/api/tle")
    assert response.status_code == 200
    assert response.json() == []


def test_list_tle_with_data(client, db):
    """
    Insert a satellite into the database,
    then verify that /api/tle returns exactly one result
    """
    db.add(Tle(satellite_id="25544", name="ISS", line1="1 25544", line2="2 25544", source_group="stations"))
    db.flush()

    response = client.get("/api/tle")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_list_tle_filter_group(client, db):
    """
    Place 2 satellites in different groups (stations and active),
    then verify that the ?group=stations parameter filters correctly
    and returns only the correct satellite
    """
    db.add(Tle(satellite_id="25544", name="ISS", line1="1 25544", line2="2 25544", source_group="stations"))
    db.add(Tle(satellite_id="25338", name="NOAA 15", line1="1 25338",line2="2 25338", source_group="active"))
    db.flush()

    response = client.get("/api/tle?group=stations")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["satellite_id"] == "25544"


def test_get_tle_found(client, db):
    """
    Add a satellite, then verify that /api/tle/25544
    returns the correct satellite with the correct name
    """
    db.add(Tle(satellite_id="25544", name="ISS", line1="1 25544", line2="2 25544", source_group="stations"))
    db.flush()

    response = client.get("/api/tle/25544")
    assert response.status_code == 200
    assert response.json()["name"] == "ISS"


def test_get_tle_not_found(client):
    """
    Verify that /api/tle/UNKNOWN
    returns a 404 error when the satellite doesn't exist
    """
    response = client.get("/api/tle/INCONNU")
    assert response.status_code == 404
