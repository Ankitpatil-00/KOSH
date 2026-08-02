from knowledge.extractor import MedicalEntityExtractor
from knowledge.builder.document_builder import KnowledgeDocumentBuilder


class KnowledgeService:

    def __init__(self):
        self.extractor = MedicalEntityExtractor()
        self.builder = KnowledgeDocumentBuilder()

    def extract(self, text: str):
        return self.extractor.extract(text)

    def process(self, article):

        entities = self.extract(article["abstract"])

        knowledge_document = self.builder.build(
            article,
            entities
        )
        
        return knowledge_document