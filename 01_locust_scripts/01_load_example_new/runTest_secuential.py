"""Este fichero representa el escenario de una prueba, que incluye:
    - 2 Clases donde se representan los grupos de hilos (Threads en Jmeter)
    - Cada grupo hereda un perfil concreto implementado en una clase aparte (Admins y Users)
    - Cada grupo de usuarios que ejecutan unos casos de uso concretos
    - La distribución de la carga entre los casos de uso de cada grupo se representa con los pesos

"""
# Example in command line:
# locust -f runTest.py --host http://localhost:8080/api/v3 -u 10 -t 20 --processes 4 --autostart --autoquit 3

from tasks.actions_user import ActionsOnUser
from authentication.users_login import UsersAdmin


class ThreadGroupForAdmins(UsersAdmin):
    tasks = {
        ActionsOnUser.delete_user: 6,
        ActionsOnUser.modify_user: 4,
        ActionsOnUser.create_user: 2,
    }
