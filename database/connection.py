from pymongo import MongoClient
from loguru import logger

import config.settings as settings


class MongoDBConnection:

    def __init__(self):
        self.client = None
        self.database = None
        logger.info("MongoDB Connection Initialized")

    def connect(self):
        logger.info("Connecting to MongoDB...")

        self.client = MongoClient(settings.MONGO_URI)
        self.database = self.client[settings.MONGO_DATABASE]

        logger.info(f"Connected to database: {settings.MONGO_DATABASE}")

        return self.database

    def close(self):
        if self.client:
            self.client.close()
            logger.info("MongoDB connection closed")