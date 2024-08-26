
from locust import HttpUser, between, log
from libraries.user_interfaz import UserInterfaz
from libraries.logModule import LogType, Logger
from locust.exception import StopUser


# Clase para instanciar usuarios registrados en mi app que heredan de AbstractUser
class UsersAdmin(UserInterfaz):
    abstract = True
    wait_time = between(3, 5)

    def on_start(self):

        with self.client.post("/api/login", data=
        {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }, catch_response=True) as response:
            self.verify_login(response)

    def verify_login(self, response):
        try:
            Logger.log_message("Un usuario de usersAdmin hace login con response: " + str(response.status_code))
            if response.status_code == 200:  # Entonces almaceno la información gracias a los atributos heredados del
                #setattr(HttpUser,"token", response.json()['token'])
                Logger.log_message("tiene token: " + str(response.json()['token']))
        except:
            Logger.log_message("Registro failed " + str(response.status_code))

    def on_stop(self):
        pass  # Simplemente termina el usuario. Aquí iría el rampdown.
