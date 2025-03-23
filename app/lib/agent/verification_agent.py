from typing import Any, List, Optional

from agents import Agent, ModelSettings

from app.config.base import BaseVerificationResult


class VerificationAgent(Agent):
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
    ):
        """
        Initialize the HypoGeneratorAgent with model settings and tools.

        Args:
            model_settings: Configuration for the model
            tools: Additional tools the agent can use
        """
        # Get the schema path using the centralized config function
        super().__init__(
            name="Verify an argument if correct and have an conclusion",
            instructions="Based on the question and hypo varify if the factor is ture or false",
            model_settings=model_settings or ModelSettings(),
            tools=tools or [],
            output_type=BaseVerificationResult,
        )
