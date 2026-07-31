import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read values from .env
PUBMED_EMAIL = os.getenv("PUBMED_EMAIL")
PUBMED_API_KEY = os.getenv("PUBMED_API_KEY")

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

PUBMED_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

REQUEST_TIMEOUT = 30

MAX_RETRIES = 3

BACKOFF_FACTOR = 1