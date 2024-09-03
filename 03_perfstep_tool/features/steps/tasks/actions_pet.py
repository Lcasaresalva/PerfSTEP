
from locust import task, SequentialTaskSet


class ActionsOnPet(SequentialTaskSet):

    def on_start(self):
        pass

    @task(45)
    def find_pet(self):
        pet_id = 1
        response = self.client.get(f"/pet/{pet_id}", headers=self.headers)
        print(response.request.headers)

    @task(45)
    def update_pet(self):
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
        self.client.put("/pet", json=body)

    @task(45)
    def create_pet(self):
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
        self.client.put("/pet", json=body)

