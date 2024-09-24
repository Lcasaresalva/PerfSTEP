
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
