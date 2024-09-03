
from locust import task, HttpUser, between


class GETRequestsHost(HttpUser):
    wait_time = between(1, 5)
    abstract = True
    endpoint = None

    @task
    def get_request(self):
        self.client.get(self.endpoint)


class POSTRequestsHost(HttpUser):
    wait_time = between(1, 5)
    abstract = True
    endpoint = None

    @task
    def post_request(self):
        self.client.post(self.endpoint)