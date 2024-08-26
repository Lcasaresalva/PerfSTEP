"""Este módulo representa el escenario de una prueba, que incluye:
    1- Tareas que se realizan una sola vez antes de comenzar la ejecución y después de finalizar
    2- Clases donde se representan los grupos de hilos de Jmeter que son:
        - Hilos con un perfil concreto predefinido en una clase aparte, de la que están heredando
        - Hilos que hacen unas tareas concretas traídas de una clase previamente definida como TaskSet
        - Cda grupo tiene un peso concreto

"""

from tasks.actions_resources import ActionsOnResources
from tasks.actions_users import ActionsOnUsers
from authentication.users_login import UsersAdmin, UsersGranted


class ThreadGroupForAdmins(UsersAdmin):
    UsersAdmin.tasks = {
        ActionsOnResources.return_inventory: 2,
        ActionsOnUsers.modify_user: 2,
        ActionsOnResources.order_store: 1,
    }


class ThreadGroupForUsers(UsersGranted):
    UsersGranted.tasks = {
        ActionsOnUsers.create_user: 2,
        ActionsOnResources.update_pet: 2,
        ActionsOnResources.find_pet: 2,
        ActionsOnResources.delete_order: 2
    }