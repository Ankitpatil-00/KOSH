from loguru import logger
import config.settings as settings

from knowledge.engines.spacy_engine import SpacyEngine
from knowledge.engines.biobert_engine import BioBertEngine
from knowledge.processors.token_cleaner import TokenCleaner
from knowledge.processors.duplicate_remover import DuplicateRemover
from knowledge.processors.confidence_filter import ConfidenceFilter
from knowledge.processors.entity_normalizer import EntityNormalizer



class MedicalEntityExtractor:

    def __init__(self):
        logger.info("Medical Entity Extractor Initialized")

        engine_name = settings.NLP_ENGINE.lower()
        self.token_cleaner = TokenCleaner()
        self.entity_normalizer = EntityNormalizer()
        self.duplicate_remover = DuplicateRemover()
        self.confidence_filter = ConfidenceFilter()
        

        if engine_name == "spacy":
            self.engine = SpacyEngine()

        elif engine_name == "biobert":
            self.engine = BioBertEngine()

        elif engine_name == "scispacy":
            from knowledge.engines.scispacy_engine import SciSpaCyEngine
            self.engine = SciSpaCyEngine()

        else:
            raise ValueError(f"Unsupported NLP engine: {engine_name}")

        logger.info(f"Using NLP Engine: {engine_name}")

    def extract(self, text: str):

        entities = self.engine.extract_entities(text)
        entities = self.token_cleaner.clean(entities)
        entities = self.entity_normalizer.clean(entities)
        entities = self.duplicate_remover.clean(entities)
        entities = self.confidence_filter.clean(entities)

        return entities