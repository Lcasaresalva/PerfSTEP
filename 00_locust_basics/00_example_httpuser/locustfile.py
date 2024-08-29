from locust import HttpUser, task


class MyHttpUser(HttpUser):
    # host = "http://localhost:8080/api/v3 "
    @task
    def order_store(self):
        body = {
            "id": 10,
            "petId": 198772,
            "quantity": 7,
            "shipDate": "2024-08-22T13:27:38.710Z",
            "status": "approved",
            "complete": True
        }
        self.client.post("/store/order", json=body)
