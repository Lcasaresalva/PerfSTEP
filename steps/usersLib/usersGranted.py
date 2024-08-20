from locust import between
from locust.exception import StopUser
from usersLib.userInterfaz import UserInterfaz
from usersLib.logModule import LogType, Logger


class UsersGranted(UserInterfaz):
    wait_time = between(1, 3)
    abstract = True

    def on_start(self):

        with self.client.post("/api/users", data = {"name":"morpheus","job":"leader"}, catch_response=True) as response:
            self.verifyLoginSuccess(response)

    def verifyLoginSuccess(self, response):
        try:
            Logger.log_message( "Un  users granted se ha creado, respuesta 201 esperada: " + str(response))
            if response.status_code == 201:  #Entonces almaceno la información gracias a los atributos heredados del httpuser
               # setattr(HttpUser, "userId", response.json()['id'])
                Logger.log_message("user creado con id: " + str(response.json()['id']))
        except:
            Logger.log_message("Creation failed" + str(response))
            #raise StopUser  #Excepción de Locust para parar el usuario y hacerlo salir, implementarla

    def on_stop(self):
        pass  #Simplemente termina el usuario.
