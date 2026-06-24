import random

PET_NAMES = ["Bella", "Charlie", "Luna"]
BREEDS = ["labrador", "husky", "beagle"]
STATUSES = ["available", "pending", "sold"]


def random_pet():
    pet_id = random.randint(1000, 999999)
    name = random.choice(PET_NAMES)
    breed = random.choice(BREEDS)

    pet = {
        "id": pet_id,
        "category": {
            "id": 1,
            "name": breed
        },
        "name": f"{name}",
        "photoUrls": [
            f"https://example.com/pets/{pet_id}.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "friendly"
            }
        ],
        "status": random.choice(STATUSES),
    }

    return pet
