
from locust import task, HttpUser, between


class GETRequestsHost(HttpUser):
    wait_time = between(1, 5)
    endpoint = None
    body = None
    headers = None

    @task
    def get_request(self):
        self.client.get(self.endpoint, headers=self.headers, json=self.body)


class POSTRequestsHost(HttpUser):
    wait_time = between(1, 5)
    endpoint = None
    body = None
    headers = None

    @task
    def post_request(self):
        self.client.post(self.endpoint, headers=self.headers, json=self.body)
