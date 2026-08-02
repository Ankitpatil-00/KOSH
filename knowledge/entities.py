from dataclasses import dataclass


@dataclass
class MedicalEntity:
    text: str
    label: str
    start: int
    end: int
    confidence: float = 1.0