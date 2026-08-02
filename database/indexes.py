from pymongo import ASCENDING

from config.logging import logger

class DatabaseIndexes:
    def __init__(self, database):

        self.database = database

        self.collection = database["articles"]
    
    def create_indexes(self):

        logger.info("Creating MongoDB indexes...")

        self.collection.create_index(

            [("pmid", ASCENDING)],

            unique=True,

            name="pmid_unique"

        )

        logger.info("PMID unique index created")
