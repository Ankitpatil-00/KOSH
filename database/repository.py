from pymongo import results
from pymongo import results
from config.settings import MONGO_COLLECTION

from config.logging import logger

class ArticleRepository:
    def __init__(self, database):

        self.collection = database[MONGO_COLLECTION]

        logger.info("Article Repository Initialized")
    
    def insert_article(self, article):

        logger.info(
            f"Upserting article {article['pmid']}"
        )

        result = self.collection.update_one(

            {"pmid": article["pmid"]},

            {
                "$set": article
            },

            upsert=True

        )

        return result
