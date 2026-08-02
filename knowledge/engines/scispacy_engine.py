from loguru import logger

from knowledge.engines.base import MedicalNlpEngine


class SciSpaCyEngine(MedicalNlpEngine):

    def __init__(self):
        logger.info("SciSpaCy Engine Initialized")

    def extract_entities(self, text: str):
        logger.info("SciSpaCy extracting entities...")

        return []