"""
Fichero locust desde el que se pueden realizar peticiones a un endpoint,
en este caso se ha implementado un ejemplo con un POST
El código está implemntado en la clase importada
"""
# Example in command line with autoquit to avoid the usage of ctrl+c:
# locust -f runTest.py --host http://localhost:8080/api/v3 -u 10 -r 2 -t 20 --processes -1 --autostart --autoquit 3


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
        POSTRequestsHost.request:1
    }

