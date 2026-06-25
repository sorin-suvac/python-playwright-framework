import random

from api.models.category import Category
from api.models.pet import Pet
from api.models.tag import Tag

PET_NAMES = ["Bella", "Charlie", "Luna"]
BREEDS = ["labrador", "husky", "beagle"]
STATUSES = ["available", "pending", "sold"]


def generate_random_pet() -> Pet:
    pet_id = random.randint(1000, 999999)
    name = random.choice(PET_NAMES)
    breed = random.choice(BREEDS)

    return Pet(
        id=pet_id,
        category=Category(id=1, name=breed),
        name=name,
        photoUrls=[f"https://example.com/pets/{pet_id}.jpg"],
        tags=[Tag(id=1, name="friendly"), Tag(id=2, name="cute")],
        status=random.choice(STATUSES),
    )
