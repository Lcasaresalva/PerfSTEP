
from locust import task, TaskSet


class ActionsOnUsers(TaskSet):

    @task(20)
    def get_users_list(self):
        self.client.get("/api/users?page=2")

    @task(30)
    def get_user_info(self):
        self.client.get("/api/users/2")

    @task(20)
    def create_user(self):
        self.client.post("/api/users", data='''
        {
            "name": "morpheus",
            "job": "leader"
        }
         ''')

    @task(10)
    def update_user(self):
        self.client.put("/api/users/2", data='''
        {
            "name": "morpheus",
            "job": "zion resident"
        }
        ''')

    @task(5)
    def patch_user(self):
        self.client.patch("/api/users/2", data='''
        {
            "name": "morpheus",
            "job": "zion resident"
        }
        ''')

    @task(5)
    def delete_user(self):
        self.client.delete("/api/users/2")
