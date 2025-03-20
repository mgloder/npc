from fastapi.testclient import TestClient

from app.models.npc import NPCPersonality, NPCStats


def test_create_and_get_npc(client: TestClient):
    # Create a test NPC
    npc_data = {
        "name": "Test NPC",
        "description": "A test NPC for unit testing",
        "personality": {
            "friendliness": 0.7,
            "aggressiveness": 0.3,
            "helpfulness": 0.8,
            "curiosity": 0.5
        },
        "stats": {
            "health": 100,
            "strength": 50,
            "intelligence": 70,
            "speed": 60
        },
        "dialogue_options": ["Hello!", "How can I help?", "Goodbye!"]
    }
    
    # Create the NPC
    response = client.post("/api/v1/npcs/", json=npc_data)
    assert response.status_code == 201
    created_npc = response.json()
    npc_id = created_npc["id"]
    
    # Get the NPC
    response = client.get(f"/api/v1/npcs/{npc_id}")
    assert response.status_code == 200
    retrieved_npc = response.json()
    
    # Verify the NPC data
    assert retrieved_npc["name"] == npc_data["name"]
    assert retrieved_npc["description"] == npc_data["description"]
    assert retrieved_npc["personality"] == npc_data["personality"]
    assert retrieved_npc["stats"] == npc_data["stats"]
    assert retrieved_npc["dialogue_options"] == npc_data["dialogue_options"] 