from sources.pubmed.search import PubMedSearch
from sources.pubmed.fetch import PubMedFetch


class PubMedService:

    def __init__(self):
        self.search = PubMedSearch()
        self.fetch = PubMedFetch()

    def collect(self, query, max_results=10):
        pmids = self.search.search(query, max_results)
        return self.fetch.fetch(pmids)