from sources.pubmed.search import PubMedSearch
from sources.pubmed.fetch import PubMedFetch
from config.logging import logger


def main():

    logger.info("Medical Research Data Collector Started")

    search = PubMedSearch()
    fetch = PubMedFetch()

    pmids = search.search(
        keyword="artificial intelligence",
        max_results=2
    )

    print("\nRetrieved PMIDs:\n")
    print(pmids)

    articles = fetch.fetch(pmids)

    print("\nRetrieved Articles:\n")

    for article in articles:
        print(article)


if __name__ == "__main__":
    main()