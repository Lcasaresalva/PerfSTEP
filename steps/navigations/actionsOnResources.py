from locust import task, SequentialTaskSet,log


class ActionsOnResources(SequentialTaskSet):

    def on_start(self):
        #habría que poner aquí las cookies de sesión para pasárselas al user en la llamada a esta clase
       #self.header = UtilHelper.get_base_header_with_cookie(self.user.get_cookie())
        pass

    @task(3)
    def listallresources(self):
        with self.client.get("/api/unknown", catch_response=True) as response:
            if response.status_code != 200:
                response.fail("Status code {}".format(response.status_code))


    @task(6)
    def getsingleresource(self):

        with self.client.get("/api/unknown/2", catch_response=True) as response:
            if response.status_code != 200:
                response.fail("Status code {}".format(response.status_code))

    @task(1)
    def getwrongresource(self):
        self.client.get("/api/unknown/23")
    @task
    def exit_task_execution(self):
        self.interrupt()