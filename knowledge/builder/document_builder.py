from knowledge.models import KnowledgeDocument


class KnowledgeDocumentBuilder:

    def build(self, article, entities):

        return KnowledgeDocument(

            pmid=article["pmid"],

            title=article["title"],

            abstract=article["abstract"],

            entities=entities,

            metadata={

                "journal": article.get("journal"),

                "publication_date": article.get("publication_date"),

                "authors": article.get("authors", [])

            }

        )