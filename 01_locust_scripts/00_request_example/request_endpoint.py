from locust import task, HttpUser, between


class GETRequestsHost(HttpUser):
    wait_time = between(1, 5)
    endpoint = None

    @task
    def request(self):
        self.client.get(self.endpoint)


class POSTRequestsHost(HttpUser):
    wait_time = between(1, 5)
    endpoint = None
    body = None

    @task
    def request(self):
        self.client.post(self.endpoint, json=self.body)
