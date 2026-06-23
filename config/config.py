import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("TEST_BASE_URL")
USERNAME = os.getenv("TEST_USERNAME")
PASSWORD = os.getenv("TEST_PASSWORD")
