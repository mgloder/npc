from typing import Dict, List, Optional
import uuid

from app.models.npc import NPC, NPCCreate, NPCUpdate


# In-memory database for demonstration
npc_db: Dict[str, NPC] = {}


async def get_npcs() -> List[NPC]:
    """Get all NPCs"""
    return list(npc_db.values())


async def get_npc(npc_id: str) -> Optional[NPC]:
    """Get an NPC by ID"""
    return npc_db.get(npc_id)


async def create_npc(npc_data: NPCCreate) -> NPC:
    """Create a new NPC"""
    npc_id = str(uuid.uuid4())
    npc = NPC(id=npc_id, **npc_data.dict())
    npc_db[npc_id] = npc
    return npc


async def update_npc(npc_id: str, npc_data: NPCUpdate) -> Optional[NPC]:
    """Update an existing NPC"""
    if npc_id not in npc_db:
        return None
    
    stored_npc = npc_db[npc_id]
    update_data = npc_data.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(stored_npc, field, value)
    
    npc_db[npc_id] = stored_npc
    return stored_npc


async def delete_npc(npc_id: str) -> bool:
    """Delete an NPC"""
    if npc_id not in npc_db:
        return False
    
    del npc_db[npc_id]
    return True 