import pytest
import pytest_asyncio
from app.modules.character.models.character import Character, Status, Gender


@pytest_asyncio.fixture
async def character(session):
    char = Character(
        external_id=1,
        name="Rick Sanchez",
        status=Status.ALIVE,
        species="Human",
        gender=Gender.MALE,
        image="https://example.com/rick.jpeg",
        url="https://rickandmortyapi.com/api/character/1",
    )
    session.add(char)
    await session.commit()
    await session.refresh(char)
    return char


class TestGetCharacters:
    async def test_returns_200(self, client):
        response = await client.get("/api/characters/")
        assert response.status_code == 200

    async def test_returns_empty_list(self, client):
        response = await client.get("/api/characters/")
        assert response.json() == []

    async def test_returns_one_character(self, client, character):
        response = await client.get("/api/characters/")
        assert len(response.json()) == 1

    async def test_limit(self, client, session):
        for i in range(5):
            session.add(Character(
                external_id=i + 1,
                name=f"Character {i}",
                status=Status.ALIVE,
                species="Human",
                gender=Gender.MALE,
                image=f"https://example.com/{i}.jpeg",
                url=f"https://example.com/character/{i}",
            ))
        await session.commit()

        response = await client.get("/api/characters/?limit=2")
        assert response.status_code == 200
        assert len(response.json()) == 2

    async def test_offset(self, client, session):
        for i in range(3):
            session.add(Character(
                external_id=i + 1,
                name=f"Character {i}",
                status=Status.ALIVE,
                species="Human",
                gender=Gender.MALE,
                image=f"https://example.com/{i}.jpeg",
                url=f"https://example.com/character/{i}",
            ))
        await session.commit()

        response = await client.get("/api/characters/?offset=2")
        assert len(response.json()) == 1


class TestGetCharacter:
    async def test_returns_200(self, client, character):
        response = await client.get(f"/api/characters/{character.id}")
        assert response.status_code == 200

    async def test_returns_correct_data(self, client, character):
        response = await client.get(f"/api/characters/{character.id}")
        data = response.json()
        assert data["name"] == "Rick Sanchez"
        assert data["status"] == "Alive"

    async def test_not_found(self, client):
        response = await client.get("/api/characters/99999")
        assert response.status_code == 404


class TestUpdateCharacter:
    async def test_returns_200(self, client, character):
        response = await client.patch(
            f"/api/characters/{character.id}",
            json={"name": "Morty Smith"}
        )
        assert response.status_code == 200

    async def test_updates_only_passed_field(self, client, character):
        await client.patch(
            f"/api/characters/{character.id}",
            json={"name": "Morty Smith"}
        )
        response = await client.get(f"/api/characters/{character.id}")
        data = response.json()
        assert data["name"] == "Morty Smith"
        assert data["species"] == "Human"  # не тронулось

    async def test_not_found(self, client):
        response = await client.patch(
            "/api/characters/99999",
            json={"name": "Nobody"}
        )
        assert response.status_code == 404

class TestDeleteCharacter:
    async def test_returns_200(self, client, character):
        response = await client.delete(f"/api/characters/{character.id}")
        assert response.status_code == 204

    async def test_actually_deleted(self, client, character):
        await client.delete(f"/api/characters/{character.id}")
        response = await client.get(f"/api/characters/{character.id}")
        assert response.status_code == 404

    async def test_not_found(self, client):
        response = await client.delete("/api/characters/99999")
        assert response.status_code == 404