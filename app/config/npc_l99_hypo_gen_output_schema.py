from pydantic import BaseModel


class HierarchicalHypo(BaseModel):
    hypothesis: str
    explanation: str
