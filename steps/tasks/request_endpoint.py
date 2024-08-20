from locust import task, HttpUser, between
from locust.exception import StopUser


class GETRequestsHost(HttpUser):
    wait_time = between(1, 5)
    abstract = True
    endpoint = None
    user = None


    @task
    def get_request(self):
        self.client.get(self.endpoint)


class POSTRequestsHost(HttpUser):
    wait_time = between(1, 5)
    abstract = True
    endpoint = None

    def on_start(self):
        data = '''
           {
               "email": "eve.holt@reqres.in",
               "password": "cityslicka"
           }
       '''
        self.client.post("/api/login", data=data)

    @task
    def post_request(self):
        self.client.post(self.endpoint)
