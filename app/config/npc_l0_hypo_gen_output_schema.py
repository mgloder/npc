from typing import List

from pydantic import BaseModel


class SupportingFactor(BaseModel):
    factor: str
    explanation: str
    evidence: str


class CounterArguments(BaseModel):
    argument: str


class Explanations(BaseModel):
    supporting_factors: List[SupportingFactor]
    counter_arguments: List[CounterArguments]


class HierarchicalHypo(BaseModel):
    hypothesis: str
    explanations: Explanations
