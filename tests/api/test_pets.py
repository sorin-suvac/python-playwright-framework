import logging

import pytest

from api.models.pet import Pet
from data.pet_factory import generate_random_pet, STATUSES as AVAILABLE_STATUSES

logger = logging.getLogger(__name__)


@pytest.mark.api
def test_available_pets(api_client):
    response = api_client.get('./pet/findByStatus?status=available')
    assert response.status == 200
    pets = [Pet(**item) for item in response.json()]
    assert len(pets) > 0, "No available pets found"
    pet = pets[0]
    logger.info(pet)
    assert pet.id is not None
    assert pet.name is not None
    assert pet.status in AVAILABLE_STATUSES, f"{pet.status} not in {AVAILABLE_STATUSES}"


@pytest.mark.api
@pytest.mark.parametrize("pet", [generate_random_pet() for _ in range(3)])
def test_create_pet(api_client, pet):
    response = api_client.post('./pet', pet.model_dump_json())
    logger.info(response.json())
    assert response.status == 200
    pet_from_rs = Pet(**response.json())
    assert pet_from_rs == pet
