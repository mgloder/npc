from typing import Type

from pydantic import BaseModel

from app.config.npc_l0_hypo_gen_output_schema import (
    HierarchicalHypo as L0HierarchicalHypo,
)
from app.config.npc_l99_hypo_gen_output_schema import (
    HierarchicalHypo as L99HierarchicalHypo,
)


def load_hierarchical_hypo_class(npc_level: int) -> Type[BaseModel]:
    """
    Load the appropriate HierarchicalHypo class based on the NPC level.

    Args:
        npc_level: The NPC level (L0 being the smartest, L99 being the dumbest)

    Returns:
        The appropriate HierarchicalHypo class

    Raises:
        ValueError: If the NPC level is not supported
    """
    if npc_level == 0:
        return L0HierarchicalHypo
    elif npc_level == 99:
        return L99HierarchicalHypo

    return L99HierarchicalHypo
