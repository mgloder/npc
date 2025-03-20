from typing import Any, Dict, List, Optional
from uuid import uuid4

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

# Import your models and schemas here
# For example: from app.models.npc import NPC
# For example: from app.schemas.npc import NPCCreate, NPCUpdate, NPCResponse

router = APIRouter()


# Define schemas
class NPCBase(BaseModel):
    name: str
    description: str
    location: str
    occupation: str
    traits: List[str]
    goals: List[str]


class NPCCreate(NPCBase):
    pass


class NPCUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    occupation: Optional[str] = None
    traits: Optional[List[str]] = None
    goals: Optional[List[str]] = None


class NPCResponse(NPCBase):
    id: str


# In-memory database for testing
npc_db: Dict[str, Dict[str, Any]] = {}


@router.post("/", response_model=NPCResponse, status_code=status.HTTP_201_CREATED)
def create_npc(npc_data: NPCCreate) -> NPCResponse:
    """Create a new NPC"""
    npc_id = str(uuid4())
    npc = {"id": npc_id, **npc_data.dict()}
    npc_db[npc_id] = npc
    return NPCResponse(id=npc_id, **npc_data.dict())


@router.get("/", response_model=List[NPCResponse])
def get_npcs() -> List[Dict[str, Any]]:
    """Get all NPCs"""
    return list(npc_db.values())


@router.get("/{npc_id}", response_model=NPCResponse)
def get_npc(npc_id: str) -> Dict[str, Any]:
    """Get an NPC by ID"""
    if npc_id not in npc_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"NPC with ID {npc_id} not found",
        )
    return npc_db[npc_id]


@router.patch("/{npc_id}", response_model=NPCResponse)
def update_npc(npc_id: str, npc_update: NPCUpdate) -> Dict[str, Any]:
    """Update an NPC"""
    if npc_id not in npc_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"NPC with ID {npc_id} not found",
        )

    # Get the current NPC data
    npc = npc_db[npc_id]

    # Update only the fields that are provided
    update_data = {k: v for k, v in npc_update.dict().items() if v is not None}
    npc.update(update_data)

    # Save the updated NPC
    npc_db[npc_id] = npc

    return npc


@router.delete("/{npc_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_npc(npc_id: str) -> None:
    """Delete an NPC"""
    if npc_id not in npc_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"NPC with ID {npc_id} not found",
        )

    # Remove the NPC from the database
    del npc_db[npc_id]

    return None
