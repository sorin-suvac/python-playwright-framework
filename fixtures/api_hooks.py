import pytest

from api.api_client import ApiClient
from config.config import API_BASE_URL


@pytest.fixture
def api_client(playwright):
    client = ApiClient(
        playwright=playwright,
        base_url=API_BASE_URL
    )
    yield client
    client.close()
