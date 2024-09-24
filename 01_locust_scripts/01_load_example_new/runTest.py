"""Este fichero representa el escenario de una prueba, que incluye:
    - 2 Clases donde se representan los grupos de hilos (Threads en Jmeter)
    - Cada grupo hereda un perfil concreto implementado en una clase aparte (Admins y Users)
    - Cada grupo de usuarios que ejecutan unos casos de uso concretos
    - La distribución de la carga entre los casos de uso de cada grupo se representa con los pesos

"""
# Command line example in case you want to use the UI (with autoquit to avoid ctrl+c at the end of the test):
# locust -f runTest.py --host http://localhost:8080/api/v3 -u 10 -r 2 -t 20 --processes -1 --autostart --autoquit 3


from tasks.actions_pet import *
from tasks.actions_store import *
from authentication.users_login import UsersAdmin, UsersGranted


class ThreadGroupForAdmins(UsersAdmin):
    weight = 6
    tasks = {
        update_pet: 1,
        order_store: 2,
        return_inventory: 4
    }


class ThreadGroupForUsers(UsersGranted):
    weight = 4
    tasks = {
        find_pet: 1,
        delete_order: 2
    }
