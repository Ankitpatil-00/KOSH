from loguru import logger

from knowledge.engines.base import MedicalNlpEngine
from knowledge.models import MedicalEntity


class SpacyEngine(MedicalNlpEngine):

    def __init__(self):
        logger.info("SpaCy Engine Initialized")

    def extract_entities(self, text: str):
        logger.info("SpaCy extracting entities...")

        entity = MedicalEntity(
            text="Metformin",
            entity_type="DRUG",
            confidence=0.99
        )

        return [entity]