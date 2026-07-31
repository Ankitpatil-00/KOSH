from sources.pubmed.client import PubMedClient
from sources.pubmed.parser import PubMedParser

from config.logging import logger



class PubMedFetch:
    def __init__(self):

        self.client = PubMedClient()
        self.parser = PubMedParser()
        logger.info("PubMed Fetch Initialized")
    

    def fetch(self, pmids):
        logger.info(f"Fetching metadata for {len(pmids)} article(s)")
        ids = ",".join(pmids)

        params = {
            "db": "pubmed",
            "id": ids,
            "retmode": "xml"       
        }

        response = self.client.get(
            endpoint="efetch.fcgi",
            params=params
        )
        
        root = self.parser.parse_xml(response.text)
        articles = self.parser.extract_articles(root)
        results = []
        for article in articles:
            parsed_article = self.parser.extract_single_article(article)
            if parsed_article is not None:
                results.append(parsed_article)
        
        return results

