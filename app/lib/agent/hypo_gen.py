from typing import Any, List, Optional

from agents import Agent, ModelSettings

from app.config import hypo_loader


class HypoGeneratorAgent(Agent):
    """
    An agent that generates hierarchical hypotheses (hypos)
    based on user input.
    Structures information in a hierarchical format with proper
    relationships between elements.
    """

    def __init__(
        self,
        model_settings: Optional[ModelSettings] = None,
        tools: Optional[List[Any]] = None,
        npc_level: int = 99,
    ):
        """
        Initialize the HypoGeneratorAgent with model settings and tools.

        Args:
            model_settings: Configuration for the model
            tools: Additional tools the agent can use
            npc_level: Level of NPC intelligence (0 being smartest, 99 being simplest)
        """
        # Get the schema path using the centralized config function
        super().__init__(
            name="HypoGenerator",
            instructions="Generate a hypothesis based on the user's input to answer the specified question.",
            model_settings=model_settings or ModelSettings(),
            tools=tools or [],
            output_type=hypo_loader.load_hierarchical_hypo_class(npc_level),
        )
