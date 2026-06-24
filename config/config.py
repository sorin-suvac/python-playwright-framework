import os

from dotenv import load_dotenv

load_dotenv()

UI_BASE_URL = os.getenv("UI_BASE_URL")
UI_USERNAME = os.getenv("UI_USERNAME")
UI_PASSWORD = os.getenv("UI_PASSWORD")
