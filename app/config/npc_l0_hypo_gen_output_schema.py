from typing import List

from pydantic import BaseModel

from app.config.base import BaseExplanations, BaseHierarchicalHypo


class SupportingFactor(BaseModel):
    factor: str
    explanation: str


class CounterArguments(BaseModel):
    factor: str
    explanation: str


class Explanations(BaseExplanations):
    supporting_factors: List[SupportingFactor]
    counter_arguments: List[CounterArguments]


class HierarchicalHypo(BaseHierarchicalHypo):
    explanations: Explanations

    def get_factors(self) -> List[dict]:
        """
        Get all factors (supporting and counter arguments) in a standardized format.

        Returns:
            List of dictionaries with the following structure:
            [{
                "type": "support" or "against",
                "factor": str,
                "explanation": str
            }]
        """
        factors = []

        # Add supporting factors
        for sup_factor in self.explanations.supporting_factors:
            factors.append({"type": "support", "factor": sup_factor.factor, "explanation": sup_factor.explanation})

        # Add counter arguments
        for counter_factor in self.explanations.counter_arguments:
            factors.append(
                {"type": "against", "factor": counter_factor.factor, "explanation": counter_factor.explanation}
            )

        return factors
