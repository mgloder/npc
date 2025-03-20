import pytest
from fastapi import status
from fastapi.testclient import TestClient


@pytest.fixture
def npc_data() -> dict:
    return {
        "name": "Test NPC",
        "description": "A test NPC",
        "location": "Test Location",
        "occupation": "Test Occupation",
        "traits": ["friendly", "helpful"],
        "goals": ["assist players", "provide information"],
    }


def test_create_npc(client: TestClient, npc_data: dict) -> None:
    response = client.post("/npcs/", json=npc_data)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["name"] == npc_data["name"]
    assert "id" in data


def test_get_npcs(client: TestClient, npc_data: dict) -> None:
    # Create an NPC first
    client.post("/npcs/", json=npc_data)

    # Get all NPCs
    response = client.get("/npcs/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_npc(client: TestClient, npc_data: dict) -> None:
    # Create an NPC first
    create_response = client.post("/npcs/", json=npc_data)
    npc_id = create_response.json()["id"]

    # Get the NPC by ID
    response = client.get(f"/npcs/{npc_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == npc_id
    assert data["name"] == npc_data["name"]


def test_update_npc(client: TestClient, npc_data: dict) -> None:
    # Create an NPC first
    create_response = client.post("/npcs/", json=npc_data)
    npc_id = create_response.json()["id"]

    # Update the NPC
    update_data = {"name": "Updated NPC Name"}
    response = client.patch(f"/npcs/{npc_id}", json=update_data)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == npc_id
    assert data["name"] == update_data["name"]

    # Verify other fields remain unchanged
    assert data["description"] == npc_data["description"]


def test_delete_npc(client: TestClient, npc_data: dict) -> None:
    # Create an NPC first
    create_response = client.post("/npcs/", json=npc_data)
    npc_id = create_response.json()["id"]

    # Delete the NPC
    response = client.delete(f"/npcs/{npc_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Verify the NPC is deleted
    get_response = client.get(f"/npcs/{npc_id}")
    assert get_response.status_code == status.HTTP_404_NOT_FOUND
