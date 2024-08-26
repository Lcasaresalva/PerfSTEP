
from locust import task, TaskSet


class ActionsOnUsers(TaskSet):

    @task(10)
    def modify_user(self):
        username = "theUser"
        body = {
          "id": 10,
          "username": "theUser",
          "firstName": "John",
          "lastName": "James",
          "email": "john@email.com",
          "password": "12345",
          "phone": "12345",
          "userStatus": 1
        }
        self.client.put(f"/user/{username}", json=body)

    @task(15)
    def create_user(self):
        body = {
          "id": 1,
          "username": "theUser2",
          "firstName": "John2",
          "lastName": "James2",
          "email": "john2@email.com",
          "password": "123456",
          "phone": "123456",
          "userStatus": 1
        }
        self.client.post("/user", json=body)
