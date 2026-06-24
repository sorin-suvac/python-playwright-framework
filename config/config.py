import os

from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")

UI_BASE_URL = os.getenv("UI_BASE_URL")
UI_USERNAME = os.getenv("UI_USERNAME")
UI_PASSWORD = os.getenv("UI_PASSWORD")
