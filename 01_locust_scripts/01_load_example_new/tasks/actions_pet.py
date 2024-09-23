
def find_pet(user):
    pet_id = 1
    response = user.client.get(f"/pet/{pet_id}", headers=user.headers)
    print(response.request.headers)


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
    response = user.client.put("/pet", json=body, headers=user.headers)
    print(response.request.headers)


def delete_order(user):
    order_id = 1
    response = user.client.delete(f"/store/order/{order_id}", headers=user.headers)
    print(response.request.headers)
