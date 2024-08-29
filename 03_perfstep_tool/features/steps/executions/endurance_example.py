"""Este módulo representa el escenario de una prueba, que incluye:
    1- Tareas que se realizan una sola vez antes de comenzar la ejecución y después de finalizar
    2- Clases donde se representan los grupos de hilos de Jmeter que son:
        - Hilos con un perfil concreto predefinido en una clase aparte, de la que están heredando
        - Hilos que hacen unas tareas concretas traídas de una clase previamente definida como TaskSet
        - Cda grupo tiene un peso concreto

"""

from tasks.actions_pet import ActionsOnPet
from tasks.actions_store import ActionsOnStore
from tasks.actions_user import ActionsOnUser
from authentication.users_login import UsersAdmin, UsersGranted


class ThreadGroupForAdmins(UsersAdmin):
    UsersAdmin.tasks = {
        ActionsOnStore.return_inventory: 2,
        ActionsOnUser.modify_user: 2,
        ActionsOnStore.order_store: 1,
    }


class ThreadGroupForUsers(UsersGranted):
    UsersGranted.tasks = {
        ActionsOnUser.create_user: 2,
        ActionsOnPet.update_pet: 2,
        ActionsOnPet.find_pet: 2,
        ActionsOnStore.delete_order: 2
    }