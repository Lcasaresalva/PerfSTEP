from locust import task,TaskSet

class ActionsOnUsers(TaskSet):

    @task(20)
    def getuserslist(self):
        self.client.get("/api/users?page=2")

    @task(30)
    def getuserinfo(self):
        self.client.get("/api/users/2")

    @task(10)
    def getwronguser(self):
        self.client.get("/api/users/23")

    @task(20)
    def createUser(self):
        self.client.post("/api/users",data='''
        {
            "name": "morpheus",
            "job": "leader"
        }
         ''')

    @task(10)
    def updateuser(self):
        self.client.put("/api/users/2",data='''
        {
            "name": "morpheus",
            "job": "zion resident"
        }
        ''')

    @task(5)
    def updatePatchUser(self):
        self.client.patch("/api/users/2",data='''
        {
            "name": "morpheus",
            "job": "zion resident"
        }
        ''')

    @task(5)
    def deleteUser(self):
        self.client.delete("/api/users/2")