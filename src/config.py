import os

from dotenv import load_dotenv

load_dotenv()

DB_URL_SQLITE = os.environ.get("DB_URL_SQLITE")
DB_URL_MONGO = os.environ.get("DB_URL_MONGO")
