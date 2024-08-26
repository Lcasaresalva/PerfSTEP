from locust import HttpUser, task


class MyHttpUser(HttpUser):
    # host = "https://test.k6.io"
    @task
    def flip_coin(self):
        self.client.get("/flip_coin.php")
        self.client.get("/flip_coin.php?bet=heads")
