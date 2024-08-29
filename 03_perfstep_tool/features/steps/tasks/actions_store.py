
from locust import task, SequentialTaskSet


class ActionsOnStore(SequentialTaskSet):

    def on_start(self):
        pass

    @task(50)
    def return_inventory(self):
        response = self.client.get("/store/inventory", headers=self.headers)
        print(response.request.headers)

    @task(40)
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

    @task(40)
    def delete_order(self):
        order_id = 1
        self.client.delete(f"/store/order/{order_id}")
