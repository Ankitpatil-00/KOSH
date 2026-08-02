from transformers import pipeline
from loguru import logger

from knowledge.engines.base import MedicalNlpEngine
from knowledge.models import MedicalEntity


class BioBertEngine(MedicalNlpEngine):

    def __init__(self):
        logger.info("Loading BioBERT Engine...")

        self.ner = pipeline(
            "token-classification",
            model="d4data/biomedical-ner-all",
            aggregation_strategy=None
        )

        logger.info("BioBERT Engine Loaded Successfully")

    def extract_entities(self, text: str):

        logger.info("Extracting medical entities using BioBERT...")

        predictions = self.ner(text)

        entities = []

        current = None

        for prediction in predictions:

            label = prediction["entity"]

            word = prediction["word"].replace("##", "")

            entity_type = label.replace("B-", "").replace("I-", "")
            
            if label.startswith("B-"):

                if current:
                    entities.append(current)

                current = {
                    "text": word,
                    "entity_type": entity_type,
                    "confidence": float(prediction["score"])
                    }

            else:

                if current:

                    current["text"] += word

                    current["confidence"] = min(
                        current["confidence"],
                        prediction["score"]
                        )

        if current:
            entities.append(current)

        result = []

        for entity in entities:

            result.append(

                MedicalEntity(

                    text=entity["text"],

                    entity_type=entity["entity_type"],

                    confidence=round(float(entity["confidence"]), 3),

                    source="BioBERT"

                    )

            )

        return result