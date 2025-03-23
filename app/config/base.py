from typing import List

from pydantic import BaseModel


class BaseExplanations(BaseModel):
    simple_explanation: str


class BaseHierarchicalHypo(BaseModel):
    hypothesis: str
    explanations: BaseExplanations

    def get_explanation(self) -> str:
        return self.explanations.simple_explanation

    def get_factors(self) -> List:
        return []


class BaseVerificationResult(BaseModel):
    result: bool
