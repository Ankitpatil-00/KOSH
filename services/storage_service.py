from database.repository import ArticleRepository


class StorageService:

    def __init__(self, repository: ArticleRepository):
        self.repository = repository

    def save(self, article):

        return self.repository.insert_article(article)

    def save_articles(self, articles):

        for article in articles:
            self.save(article)