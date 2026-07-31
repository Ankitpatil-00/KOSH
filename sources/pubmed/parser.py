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