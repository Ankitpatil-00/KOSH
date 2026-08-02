from loguru import logger
from database.repository import ArticleRepository
from database.connection import MongoDBConnection
from services.pubmed_service import PubMedService
from services.storage_service import StorageService
from services.knowledge_service import KnowledgeService


def main():

    logger.info("Medical Research Data Collector Started")

    # -------------------------
    # Database
    # -------------------------
    connection = MongoDBConnection()
    db = connection.connect()

    repository = ArticleRepository(db)

    # -------------------------
    # Services
    # -------------------------
    pubmed_service = PubMedService()
    knowledge_service = KnowledgeService()
    storage_service = StorageService(repository)

    # -------------------------
    # Collect Articles
    # -------------------------
    articles = pubmed_service.collect(
        "diabetes",
        2
    )

    # -------------------------
    # Process Knowledge
    # -------------------------
    for article in articles:

      knowledge_document = knowledge_service.process(article)

      print(f"\nPMID: {knowledge_document.pmid}")

      print("Entities:")

      for entity in knowledge_document.entities:
          print("   ", entity)

      storage_service.save(
          knowledge_document.to_dict()
      )

    # ------------------------- 
    # Close Database
    # -------------------------
    connection.close()


if __name__ == "__main__":
    main()