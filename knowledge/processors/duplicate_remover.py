from loguru import logger


class DuplicateRemover:

    def clean(self, entities):

        logger.info("Removing duplicate entities...")

        unique = []

        seen = set()

        for entity in entities:

            key = (
                entity.text.lower(),
                entity.entity_type
            )

            if key not in seen:

                seen.add(key)

                unique.append(entity)

        return unique