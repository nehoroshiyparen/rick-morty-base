import pytest
import pytest_asyncio
from datetime import datetime, timezone
from app.modules.episode.models.episode import Episode


@pytest_asyncio.fixture
async def episode(session):
    ep = Episode(
        external_id=1,
        name="Pilot",
        episode="S01E01",
        air_date=datetime(2013, 12, 2, tzinfo=timezone.utc),
        url="https://example.com/episode/1",
        created_at=datetime(2017, 11, 10, 12, 56, 33, 798000, tzinfo=timezone.utc),
    )
    session.add(ep)
    await session.commit()
    await session.refresh(ep)
    return ep


class TestGetEpisodes:
    async def test_returns_200(self, client):
        response = await client.get("/api/episodes/")
        assert response.status_code == 200

    async def test_returns_empty_list(self, client):
        response = await client.get("/api/episodes/")
        assert response.json() == []

    async def test_returns_one_episode(self, client, episode):
        response = await client.get("/api/episodes/")
        assert len(response.json()) == 1

    async def test_limit(self, client, session):
        for i in range(5):
            session.add(Episode(
                external_id=i + 1,
                name=f"Episode {i}",
                episode=f"S01E0{i + 1}",
                url=f"https://example.com/episode/{i}",
                air_date=datetime(2013, 12, 2, tzinfo=timezone.utc),
                created_at=datetime.now(timezone.utc),
            ))

        await session.commit()

        response = await client.get("/api/episodes/?limit=2")
        assert response.status_code == 200
        assert len(response.json()) == 2

    async def test_offset(self, client, session):
        for i in range(3):
            session.add(Episode(
                external_id=i + 1,
                name=f"Episode {i}",
                episode=f"S01E0{i + 1}",
                url=f"https://example.com/episode/{i}",
                air_date=datetime(2013, 12, 2, tzinfo=timezone.utc),
                created_at=datetime.now(timezone.utc),
            ))

        await session.commit()

        response = await client.get("/api/episodes/?offset=2")
        assert len(response.json()) == 1


class TestGetEpisode:
    async def test_returns_200(self, client, episode):
        response = await client.get(f"/api/episodes/{episode.id}")
        assert response.status_code == 200

    async def test_returns_correct_data(self, client, episode):
        response = await client.get(f"/api/episodes/{episode.id}")
        data = response.json()
        assert data["name"] == "Pilot"

    async def test_not_found(self, client):
        response = await client.get("/api/episodes/99999")
        assert response.status_code == 404


class TestUpdateEpisode:
    async def test_returns_200(self, client, episode):
        response = await client.patch(
            f"/api/episodes/{episode.id}",
            json={"name": "New Episode"}
        )
        assert response.status_code == 200

    async def test_updates_only_passed_field(self, client, episode):
        await client.patch(
            f"/api/episodes/{episode.id}",
            json={"name": "New Episode"}
        )

        response = await client.get(f"/api/episodes/{episode.id}")
        data = response.json()

        assert data["name"] == "New Episode"

    async def test_not_found(self, client):
        response = await client.patch(
            "/api/episodes/99999",
            json={"name": "Ghost"}
        )
        assert response.status_code == 404


class TestDeleteEpisode:
    async def test_returns_204(self, client, episode):
        response = await client.delete(f"/api/episodes/{episode.id}")
        assert response.status_code == 204

    async def test_actually_deleted(self, client, episode):
        await client.delete(f"/api/episodes/{episode.id}")
        response = await client.get(f"/api/episodes/{episode.id}")
        assert response.status_code == 404

    async def test_not_found(self, client):
        response = await client.delete("/api/episodes/99999")
        assert response.status_code == 404