from locust import User, task, constant, between


class MyFirstTest(User):
    weight = 2
    wait_time = constant(1)

    @task
    def launch(self):
        print("MyFirstTest: Launching the URL1")

    @task
    def search(self):
        print("MyFirstTest: Searching1")


class MySecondTest(User):
    weight = 2
    wait_time = between(0.5, 1)

    @task
    def launch2(self):
        print("MySecondTest: Launching the URL2")

    @task
    def search2(self):
        print("MySecondTest: Searching2")
