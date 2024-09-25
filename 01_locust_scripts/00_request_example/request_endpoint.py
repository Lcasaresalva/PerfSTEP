from locust import task, HttpUser, between


class GETRequestsHost(HttpUser):
    # If abstract is True, the class is meant to be subclassed, and locust will not spawn users of this class during a test.
    abstract = True
    wait_time = between(1, 5)
    endpoint = None

    @task
    def request(self):
        self.client.get(self.endpoint)


class POSTRequestsHost(HttpUser):
    # If abstract is True, the class is meant to be subclassed, and locust will not spawn users of this class during a test.
    abstract = True
    wait_time = between(1, 5)
    endpoint = None
    body = None

    @task
    def request(self):
        self.client.post(self.endpoint, json=self.body)
