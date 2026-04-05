import pytest_asyncio
from app.modules.location.models.location import Location


@pytest_asyncio.fixture
async def location(session):
    loc = Location(
        external_id=1,
        name="Earth",
        type="Planet",
        dimension="Dimension C-137",
        url="https://example.com/location/1",
    )
    session.add(loc)
    await session.commit()
    await session.refresh(loc)
    return loc


class TestGetLocations:
    async def test_returns_200(self, client):
        response = await client.get("/api/locations/")
        assert response.status_code == 200

    async def test_returns_empty_list(self, client):
        response = await client.get("/api/locations/")
        assert response.json()["data"] == []

    async def test_returns_one_location(self, client, location):
        response = await client.get("/api/locations/")
        assert len(response.json()["data"]) == 1

    async def test_limit(self, client, session):
        for i in range(5):
            session.add(Location(
                external_id=i + 1,
                name=f"Location {i}",
                type="Planet",
                dimension="C-137",
                url=f"https://example.com/location/{i}",
            ))
        await session.commit()

        response = await client.get("/api/locations/?limit=2")
        assert response.status_code == 200
        assert len(response.json()["data"]) == 2

    async def test_offset(self, client, session):
        for i in range(3):
            session.add(Location(
                external_id=i + 1,
                name=f"Location {i}",
                type="Planet",
                dimension="C-137",
                url=f"https://example.com/location/{i}",
            ))
        await session.commit()

        response = await client.get("/api/locations/?offset=2")
        assert len(response.json()["data"]) == 1


class TestGetLocation:
    async def test_returns_200(self, client, location):
        response = await client.get(f"/api/locations/{location.id}")
        assert response.status_code == 200

    async def test_returns_correct_data(self, client, location):
        response = await client.get(f"/api/locations/{location.id}")
        data = response.json()["data"]
        assert data["name"] == "Earth"

    async def test_not_found(self, client):
        response = await client.get("/api/locations/99999")
        assert response.status_code == 404


class TestUpdateLocation:
    async def test_returns_200(self, client, location):
        response = await client.patch(
            f"/api/locations/{location.id}",
            json={"name": "New Earth"}
        )
        assert response.status_code == 200

    async def test_updates_only_passed_field(self, client, location):
        await client.patch(
            f"/api/locations/{location.id}",
            json={"name": "New Earth"}
        )
        response = await client.get(f"/api/locations/{location.id}")
        data = response.json()["data"]
        assert data["name"] == "New Earth"
        assert data["type"] == "Planet"  # не тронулось

    async def test_not_found(self, client):
        response = await client.patch(
            "/api/locations/99999",
            json={"name": "Nowhere"}
        )
        assert response.status_code == 404


class TestDeleteLocation:
    async def test_returns_204(self, client, location):
        response = await client.delete(f"/api/locations/{location.id}")
        assert response.status_code == 204

    async def test_actually_deleted(self, client, location):
        await client.delete(f"/api/locations/{location.id}")
        response = await client.get(f"/api/locations/{location.id}")
        assert response.status_code == 404

    async def test_not_found(self, client):
        response = await client.delete("/api/locations/99999")
        assert response.status_code == 404
