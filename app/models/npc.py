from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class NPCState(str, Enum):
    IDLE = "idle"
    PATROLLING = "patrolling"
    COMBAT = "combat"
    FLEEING = "fleeing"
    INTERACTING = "interacting"


class NPCPersonality(BaseModel):
    friendliness: float = Field(
        ..., ge=0.0, le=1.0, description="How friendly the NPC is (0-1)"
    )
    aggressiveness: float = Field(
        ..., ge=0.0, le=1.0, description="How aggressive the NPC is (0-1)"
    )
    helpfulness: float = Field(
        ..., ge=0.0, le=1.0, description="How helpful the NPC is (0-1)"
    )
    curiosity: float = Field(
        ..., ge=0.0, le=1.0, description="How curious the NPC is (0-1)"
    )


class NPCStats(BaseModel):
    health: int = Field(..., gt=0)
    strength: int = Field(..., ge=0)
    intelligence: int = Field(..., ge=0)
    speed: int = Field(..., ge=0)


class NPCBase(BaseModel):
    name: str
    description: str
    personality: NPCPersonality
    stats: NPCStats
    state: NPCState = NPCState.IDLE
    dialogue_options: List[str] = []


class NPCCreate(NPCBase):
    pass


class NPC(NPCBase):
    id: str

    class Config:
        orm_mode = True


class NPCUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    personality: Optional[NPCPersonality] = None
    stats: Optional[NPCStats] = None
    state: Optional[NPCState] = None
    dialogue_options: Optional[List[str]] = None
