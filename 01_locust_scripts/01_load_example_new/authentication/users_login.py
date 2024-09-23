
from locust import HttpUser, between, constant


class UsersAdmin(HttpUser):
    abstract = True
    # wait_time = between(3, 5)
    wait_time = constant(1)

    def on_start(self):
        self.headers = {'accept': 'application/json',  'api_key': 'admin-key'}


class UsersGranted(HttpUser):
    # wait_time = between(1, 3)
    abstract = True
    wait_time = constant(1)

    def on_start(self):
        self.headers = {'accept': 'application/json', 'api_key': 'granted-key'}
