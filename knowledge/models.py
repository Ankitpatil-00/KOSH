from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class MedicalEntity:
    text: str
    entity_type: str
    confidence: float = 1.0
    normalized_name: Optional[str] = None
    ontology_id: Optional[str] = None
    source: str = "PubMed"

    def to_dict(self):

        return {
            "text": self.text,
            "entity_type": self.entity_type,
            "confidence": self.confidence,
            "normalized_name": self.normalized_name,
            "ontology_id": self.ontology_id,
            "source": self.source
        }

@dataclass
class MedicalRelation:
    subject: MedicalEntity
    predicate: str
    object: MedicalEntity
    confidence: float = 1.0
    source: str = "PubMed"


@dataclass
class KnowledgeDocument:

    pmid: str

    title: str

    abstract: str

    entities: List[MedicalEntity] = field(default_factory=list)

    relations: List[MedicalRelation] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    def to_dict(self):

        return {

            "pmid": self.pmid,

            "title": self.title,

            "abstract": self.abstract,

            "entities": [
                entity.to_dict()
                for entity in self.entities
            ],

            "relations": [],

            "metadata": self.metadata

        }