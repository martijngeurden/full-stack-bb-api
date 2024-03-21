import os
from dotenv import load_dotenv

load_dotenv()

db_username = os.environ.get("DB_USERNAME")
db_password = os.environ.get("DB_PASSWORD")
db_hostname = os.environ.get("DB_HOSTNAME", "localhost")
documentation_url = os.environ.get("DOCS_URL", None)
cors_origins = os.environ.get("ALLOWED_ORIGINS", "*")

