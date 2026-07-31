from sources.pubmed.search import PubMedSearch
from config.logging import logger


def main():
    logger.info("Medical Research Data Collector Started")

    search = PubMedSearch()

    pmids = search.search(
        keyword="artificial intelligence",
        max_results=5
    )

    print("\nRetrieved PMIDs:\n")

    for pmid in pmids:
        print(pmid)


if __name__ == "__main__":
    main()