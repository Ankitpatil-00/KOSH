import xml.etree.ElementTree as ET

from config.logging import logger

class PubMedParser:

    def __init__(self):
        logger.info("PubMed Parser Initialized")

    def parse_xml(self, xml_text):
        logger.info("Parsing XML response")
        root = ET.fromstring(xml_text)

        return root
    
    def extract_pmids(self, root):
        logger.info("Extracting PMIDs from XML")
        id_list = root.find("IdList")

        if id_list is None:
            return []

        pmids = []
        for element in id_list.findall("Id"):
            if element.text:
                pmids.append(element.text.strip())
        
        return pmids
    
    def extract_articles(self, root):

        logger.info("Extracting articles from XML")

        articles = root.findall("PubmedArticle")

        return articles
    
    def extract_title(self, article_info):

        return article_info.findtext(
            "ArticleTitle",
            default=""
        )
    
    def extract_pmcid(self, article):
        article_id_list = article.find(".//ArticleIdList")
        if article_id_list is None:
            return None
        for article_id in article_id_list.findall("ArticleId"):
            article_id.get("IdType")

    def extract_single_article(self, article):

        logger.info("Extracting single article")

        citation = article.find("MedlineCitation")

        if citation is None:
            return None

        pmid = citation.findtext("PMID", default="")

        article_info = citation.find("Article")

        journal = ""

        journal_info = article_info.find("Journal")

        if journal_info is not None:
            journal = journal_info.findtext("Title", default="")
        
        doi = ""

        for location in article_info.findall("ELocationID"):
            if location.get("EIdType") == "doi":
                doi = location.text.strip() if location.text else ""
                break

        publication_date = ""

        journal_issue = journal_info.find("JournalIssue") if journal_info is not None else None

        if journal_issue is not None:
            pub_date = journal_issue.find("PubDate")

            if pub_date is not None:
                year = pub_date.findtext("Year", default="")
                month = pub_date.findtext("Month", default="")
                day = pub_date.findtext("Day", default="")
        if year:

            if month and day:
                publication_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"

            elif month:
                publication_date = f"{year}-{month.zfill(2)}"

            else:
                publication_date = year
        
        abstract = ""
        parts = []
        abstract_info = article_info.find("Abstract")
        if abstract_info is not None:
            
            for section in abstract_info.findall("AbstractText"):
                label = section.get("Label", "")
                text = "".join(section.itertext()).strip()
                if label:
                    parts.append(f"{label}: {text}")
                else:
                    parts.append(text)
        
        abstract = "\n\n".join(parts)

        authors = []
        author_list = article_info.find("AuthorList")

        if author_list is not None:
            for author in author_list.findall("Author"):
                fore_name = author.findtext("ForeName", default="")
                last_name = author.findtext("LastName", default="")
                full_name = f"{fore_name} {last_name}".strip()
                if full_name:
                    authors.append(full_name)


        

        if article_info is None:
            return None

        title = self.extract_title(article_info)

        return {
            "pmid": pmid,
            "title": title,
            "journal": journal,
            "doi": doi,
            "publication_date": publication_date,
            "abstract": abstract,
            "authors": authors,
            "pmcid": self.extract_pmcid(article),
        }

