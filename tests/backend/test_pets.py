import logging

import pytest

from factory.pet_factory import random_pet

logger = logging.getLogger(__name__)


@pytest.mark.api
def test_available_pets(api_client):
    response = api_client.get('./pet/findByStatus?status=available')
    logger.info(response)
    assert response.status == 200


@pytest.mark.api
@pytest.mark.parametrize("pet", [random_pet() for _ in range(3)])
def test_create_pet(api_client, pet):
    response = api_client.post('./pet', pet)
    logger.info(response)
    assert response.status == 200
