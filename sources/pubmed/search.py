from sources.pubmed.client import PubMedClient
from sources.pubmed.parser import PubMedParser
from config.logging import logger








class PubMedSearch:
    def __init__(self):
        self.client = PubMedClient()
        self.parser = PubMedParser()
        logger.info("PubMed Search Initialized")
    

    def search(self, keyword, max_results=10):

        logger.info(f"Searching PubMed for: {keyword}")

        params = {
            "db": "pubmed",
            "term": keyword,
            "retmax": max_results,
            "retmode": "xml"
        }
        
        response = self.client.get(
            endpoint="esearch.fcgi",
            params=params
        )
        root = self.parser.parse_xml(response.text)
        pmids = self.parser.extract_pmids(root)

        return pmids
        