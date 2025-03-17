import os
from dotenv import load_dotenv

# Load .env file
# load_dotenv()
load_dotenv(dotenv_path=".env.staging")


# Access variables
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
URL = os.getenv("URL")
