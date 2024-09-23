"""Este módulo representa el escenario de una prueba, que incluye:
    1- Tareas que se realizan una sola vez antes de comenzar la ejecución y después de finalizar
    2- Clases donde se representan los grupos de hilos de Jmeter que son:
        - Hilos con un perfil concreto predefinido en una clase aparte, de la que están heredando
        - Hilos que hacen unas tareas concretas traídas de una clase previamente definida como TaskSet
        - Cda grupo tiene un peso concreto

"""
# Example in command line:
# locust -f runTest.py --host http://localhost:8080/api/v3 -u 10 -t 20 --processes 4 --autostart --autoquit 3

from tasks.actions_store import *
from tasks.actions_user import ActionsOnUser
from authentication.users_login import UsersAdmin, UsersGranted


class ThreadGroupForAdmins(UsersAdmin):
    weight = 6
    UsersAdmin.tasks = {
        ActionsOnUser.create_user: 4,
        ActionsOnUser.modify_user: 2,
        ActionsOnUser.delete_user: 2,
    }


class ThreadGroupForUsers(UsersGranted):
    weight = 2
    UsersGranted.tasks = {
        return_inventory: 2
    }
