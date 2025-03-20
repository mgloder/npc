from typing import List, Optional

from fastapi import APIRouter, HTTPException, status

from app.models.npc import NPC, NPCCreate, NPCUpdate
from app.services import npc_service

router = APIRouter(prefix="/npcs", tags=["npcs"])


@router.get("/", response_model=List[NPC])
async def get_npcs():
    """Get all NPCs"""
    return await npc_service.get_npcs()


@router.get("/{npc_id}", response_model=NPC)
async def get_npc(npc_id: str):
    """Get an NPC by ID"""
    npc = await npc_service.get_npc(npc_id)
    if not npc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"NPC with ID {npc_id} not found"
        )
    return npc


@router.post("/", response_model=NPC, status_code=status.HTTP_201_CREATED)
async def create_npc(npc_data: NPCCreate):
    """Create a new NPC"""
    return await npc_service.create_npc(npc_data)


@router.patch("/{npc_id}", response_model=NPC)
async def update_npc(npc_id: str, npc_data: NPCUpdate):
    """Update an NPC"""
    npc = await npc_service.update_npc(npc_id, npc_data)
    if not npc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"NPC with ID {npc_id} not found"
        )
    return npc


@router.delete("/{npc_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_npc(npc_id: str):
    """Delete an NPC"""
    success = await npc_service.delete_npc(npc_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"NPC with ID {npc_id} not found"
        ) 