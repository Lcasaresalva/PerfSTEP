
def find_pet(user):
    pet_id = 1
    user.client.get(f"/pet/{pet_id}", headers=user.headers)


def update_pet(user):
    body = {
        "id": 10,
        "name": "doggie",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    user.client.put("/pet", json=body, headers=user.headers)

