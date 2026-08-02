import re

from loguru import logger


class EntityNormalizer:

    def clean(self, entities):

        logger.info("Normalizing medical entities...")

        normalized = []

        for entity in entities:

            text = entity.text

            # remove ##
            text = text.replace("##", "")

            # remove extra spaces
            text = re.sub(r"\s+", " ", text)

            # remove leading/trailing spaces
            text = text.strip()

            # Title Case
            text = text.title()

            entity.text = text

            normalized.append(entity)

        return normalized