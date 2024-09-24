
from locust import task, SequentialTaskSet


class ActionsOnUser(SequentialTaskSet):

    @task
    def create_user(self):
        body = {
          "id": 1,
          "username": "theUser",
          "firstName": "John",
          "lastName": "James",
          "email": "john@email.com",
          "password": "123456",
          "phone": "123456",
          "userStatus": 1
        }
        response = self.client.post("/user", json=body, headers=self.headers)
        print(response.request.headers)

    @task
    def modify_user(self):
        username = "theUser"
        body = {
          "id": 10,
          "username": "theUser2",
          "firstName": "John",
          "lastName": "James",
          "email": "john@email.com",
          "password": "12345",
          "phone": "12345",
          "userStatus": 1
        }
        response = self.client.put(f"/user/{username}", json=body, headers=self.headers)
        print(response.request.headers)

    @task
    def delete_user(self):
        username = "theUser2"
        response = self.client.delete(f"/user/{username}", headers=self.headers)
        print(response.request.headers)
