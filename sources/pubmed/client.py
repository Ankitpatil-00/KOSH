import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config.logging import logger
from config import settings

class PubMedClient:
    def __init__(self):
        
        self.base_url = settings.PUBMED_BASE_URL
        self.session = requests.Session()
        retry_strategy = Retry(
            total=settings.MAX_RETRIES,
            backoff_factor=settings.BACKOFF_FACTOR,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["GET"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)

        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

        logger.info("PubMed Client Initialized")
    
    def get(self, endpoint, params=None):

        url = self.base_url + endpoint
        logger.info(f"Sending GET request to {url}")
        
        try:
            response = self.session.get(
                url=url,
                params=params,
                timeout=settings.REQUEST_TIMEOUT
            )

            response.raise_for_status()
            logger.info(f"Response received: {response.status_code}")
            return response

        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise