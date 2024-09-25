"""Este módulo representa el escenario de una prueba, que incluye:
    1- Tareas que se realizan una sola vez antes de comenzar la ejecución y después de finalizar
    2- Clases donde se representan los grupos de hilos de Jmeter que son:
        - Hilos con un perfil concreto predefinido en una clase aparte, de la que están heredando
        - Hilos que hacen unas tareas concretas traídas de una clase previamente definida como TaskSet
        - Cda grupo tiene un peso concreto

"""

from tasks.actions_pet import *
from tasks.actions_store import *
from authentication.users_login import UsersAdmin, UsersGranted


class ThreadGroupForAdmins(UsersAdmin):
    abstract = True

    tasks = {
        update_pet: 2,
        order_store: 4,
        return_inventory: 6
    }


class ThreadGroupForUsers(UsersGranted):
    abstract = True

    tasks = {
        find_pet: 2,
        delete_order: 4
    }