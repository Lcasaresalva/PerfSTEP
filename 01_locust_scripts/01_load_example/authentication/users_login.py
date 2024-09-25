
from locust import HttpUser, constant


class UsersAdmin(HttpUser):
    abstract = True
    wait_time = constant(1)

    def on_start(self):
        self.headers = {'accept': 'application/json',  'api_key': 'admin-key'}


class UsersGranted(HttpUser):
    abstract = True
    wait_time = constant(1)

    def on_start(self):
        self.headers = {'accept': 'application/json', 'api_key': 'granted-key'}
