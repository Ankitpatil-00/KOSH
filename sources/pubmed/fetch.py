from sources.pubmed.client import PubMedClient

from config.logging import logger



class PubMedFetch:
    def __init__(self):

        self.client = PubMedClient()
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
        
        return response

