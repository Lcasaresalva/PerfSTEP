"""Este módulo representa el escenario de una prueba, que incluye:
    1- Tareas que se realizan una sola vez antes de comenzar la ejecución y después de finalizar
    2- Clases donde se representan los grupos de hilos de Jmeter que son:
        - Hilos con un perfil concreto predefinido en una clase aparte, de la que están heredando
        - Hilos que hacen unas tareas concretas traídas de una clase previamente definida como TaskSet
        - Cda grupo tiene un peso concreto

"""
# Example in command line:
# locust -f runTest.py --host https://reqres.in -u 10 -t 20 --processes 4 --autostart --autoquit 3

import logging
from locust import events
from locust.runners import WorkerRunner

from tasks.actions_resources import ActionsOnResources
from tasks.actions_users import ActionsOnUsers
from libraries.users_admin import UsersAdmin
from libraries.users_granted import UsersGranted

CPU_WARNING_THRESHOLD = 1.5
CPU_MONITOR_INTERVAL = 0.9


class ThreadGroupForAdmins(UsersAdmin):
    UsersAdmin.tasks = {
        ActionsOnUsers.create_user: 2,  # post
        ActionsOnUsers.update_user: 2,  # put
        ActionsOnUsers.delete_user: 1,  # delete
        ActionsOnUsers.patch_user: 1  # patch
    }


class ThreadGroupForUsers(UsersGranted):
    UsersGranted.tasks = {ActionsOnResources.get_single_resource: 2, ActionsOnResources.get_wrong_resource: 2}


# Only when running this file:
@events.quitting.add_listener
def _(environment, **kwargs):
    fail_criteria = []
    errors = 0

    if environment.stats.total.get_response_time_percentile(0.95) > 100:
        fail_criteria.append('95th percentile response time > 100 ms')
        errors += 1
    if environment.stats.total.avg_response_time > 150:
        fail_criteria.append('Average response time ratio > 150 ms')
        errors += 1
    if environment.stats.total.fail_ratio >= 0.05:
        fail_criteria.append('Error ratio exceeds 5%')
        errors += 1

    # Sólo el master reporta los NFRs fallidos
    if not isinstance(environment.runner, WorkerRunner):
        logging.error('NFRs fully met!') if errors < 1 else print(f'{errors} NFRs failed during this run: \n')
        for error in fail_criteria:
            logging.error(error)


@events.quit.add_listener
def quit_test(exit_code: int):
    # runner = environment.runner
    #  if not (isinstance(runner, WorkerRunner)):
    print(f" Locust has shut down with code: {exit_code}")


@events.test_stopping.add_listener
def test_stopping(environment, **_kwargs):
    print('Test stopping')  # cuando termina el tiempo de ejecución


@events.test_stop.add_listener
def test_stop(environment, **_kwargs):
    print("test run stopped")  # una vez parado tras el tiempo de ejecución
