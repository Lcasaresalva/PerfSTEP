"""Este módulo representa el escenario de una prueba, que incluye:
    1- Tareas que se realizan una sola vez antes de comenzar la ejecución y después de finalizar
    2- Clases donde se representan los grupos de hilos de Jmeter que son:
        - Hilos con un perfil concreto predefinido en una clase aparte, de la que están heredando
        - Hilos que hacen unas tareas concretas traídas de una clase previamente definida como TaskSet
        - Cda grupo tiene un peso concreto

"""
from typing import List

from usersLib.usersGranted import UsersGranted
from usersLib.usersAdmin import UsersAdmin
from navigations.actionsOnUsers import ActionsOnUsers
from navigations.actionsOnResources import ActionsOnResources
from locust import events
import logging


# # Aquí cargamos los usuarios de un csv, en este caso llamamos al login del ejemplo que va directo con user/pwd
# @events.test_start.add_listener
# def on_test_start(self):
#     print("Inicializando la prueba...")
#
#
# @events.test_stop.add_listener
# def on_test_stop(self):
#     print("Fin de la prueba...")


class ThreadGroupForAdmins(UsersAdmin):
    UsersAdmin.tasks = {
        # ActionsOnResources.getsingleresource: 1,
        #ActionsOnUsers.getuserinfo: 5
        ActionsOnUsers.createUser: 2,  # post
        ActionsOnUsers.updateuser: 2,  # put
        ActionsOnUsers.deleteUser: 1,  # delete
        ActionsOnUsers.updatePatchUser: 1  #patch
    }

@events.quit.add_listener
def quit(exit_code: int, **_kwargs):
    print(f" Locust has shut down with code: {exit_code}")  #con el crl+C tras recopilar métricas


@events.test_stopping.add_listener
def test_stopping(environment, **_kwargs):
    print('Test stopping')  #cuando termina el tiempo de ejecución


@events.test_stop.add_listener
def test_stop(environment, **_kwargs):
    print("test run stopped")  #una vez parado tras el tiempo de ejecución


class ThreadGroupForUsers(UsersGranted):
    UsersGranted.tasks = {ActionsOnResources.getsingleresource: 2, ActionsOnResources.getwrongresource: 2}
