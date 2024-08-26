
from locust import task, HttpUser, between


class RequestsHost(HttpUser):
    wait_time = between(1, 5)
    abstract = True
    endpoint = None
    body = None

    @task
    def get_request(self):
        self.client.get(self.endpoint)

    @task
    def post_request(self):
        self.client.post(self.endpoint, json=self.body)
