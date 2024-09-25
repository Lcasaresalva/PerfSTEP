
from locust import HttpUser, between
from behave.configuration import Configuration

conf = Configuration()


class UsersAdmin(HttpUser):
    wait_time = between(3, 5)

    def on_start(self):
        api_key = conf.userdata["user_admin_key"]
        self.headers = {'accept': 'application/json',  'api_key': api_key}


class UsersGranted(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        api_key = conf.userdata["user_granted_key"]
        self.headers = {'accept': 'application/json', 'api_key': api_key}
