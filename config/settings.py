import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# PubMed
PUBMED_EMAIL = os.getenv("PUBMED_EMAIL")
PUBMED_API_KEY = os.getenv("PUBMED_API_KEY")
PUBMED_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

# MongoDB
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DATABASE = os.getenv("MONGO_DATABASE")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

# NLP
NLP_ENGINE = os.getenv("NLP_ENGINE", "spacy")

# HTTP
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
BACKOFF_FACTOR = 1