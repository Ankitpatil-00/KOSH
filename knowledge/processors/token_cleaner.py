from loguru import logger


class TokenCleaner:

    def clean(self, entities):

        logger.info("Cleaning WordPiece tokens...")

        cleaned = []

        for entity in entities:

            entity.text = entity.text.replace("##", "")

            cleaned.append(entity)

        return cleaned