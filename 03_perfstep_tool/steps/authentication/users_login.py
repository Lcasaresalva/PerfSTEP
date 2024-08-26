
from locust import HttpUser, between


class UsersAdmin(HttpUser):
    abstract = True
    wait_time = between(3, 5)

    def on_start(self):
        self.headers = {'accept': 'application/json',  'api_key': 'admin-key'}


class UsersGranted(HttpUser):
    wait_time = between(1, 3)
    abstract = True

    def on_start(self):
        self.headers = {'accept': 'application/json', 'api_key': 'granted-key'}
