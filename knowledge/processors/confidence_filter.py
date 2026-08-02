from loguru import logger


class ConfidenceFilter:

    def __init__(self, threshold=0.80):

        self.threshold = threshold

    def clean(self, entities):

        logger.info(
            f"Filtering entities below {self.threshold}"
        )

        return [
            entity
            for entity in entities
            if entity.confidence >= self.threshold
        ]