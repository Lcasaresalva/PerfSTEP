
def return_inventory(self):
    response = self.client.get("/store/inventory", headers=self.headers)
    print(response.request.headers)


def order_store(self):
    body = {
      "id": 10,
      "petId": 198772,
      "quantity": 7,
      "shipDate": "2024-08-22T13:27:38.710Z",
      "status": "approved",
      "complete": True
    }
    response = self.client.post("/store/order", json=body, headers=self.headers)
    print(response.request.headers)


def delete_order(self):
    order_id = 1
    response = self.client.delete(f"/store/order/{order_id}", headers=self.headers)
    print(response.request.headers)
