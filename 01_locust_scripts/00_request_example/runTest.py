"""Este módulo representa el escenario de una prueba, que incluye:
    1- Tareas que se realizan una sola vez antes de comenzar la ejecución y después de finalizar
    2- Clases donde se representan los grupos de hilos de Jmeter que son:
        - Hilos con un perfil concreto predefinido en una clase aparte, de la que están heredando
        - Hilos que hacen unas tareas concretas traídas de una clase previamente definida como TaskSet
        - Cda grupo tiene un peso concreto

"""
# Example in command line:
# locust -f runTest.py --host http://localhost:8080/api/v3 -u 10 -t 20 --processes 4 --autostart --autoquit 3


from request_endpoint import POSTRequestsHost


class RequestTasks(POSTRequestsHost):
    endpoint = '/store/order'
    body = {"id": 10,
            "petId": 198772,
            "quantity": 7,
            "shipDate": "2024-08-23T07:10:50.200Z",
            "status": "approved",
            "complete": True
            }

    tasks = {
        POSTRequestsHost.request: 1
    }

