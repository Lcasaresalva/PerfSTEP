from behave import step

from executions.request_endpoint import *
from execution_lib import execute_locust_tasks


@step('I execute the "{request}" to "{endpoint}" endpoint')
def execute_locust_task(context, request, endpoint):

    context.host = "http://localhost:8080/api/v3"
    task_class_name = f'{request}RequestsHost'
    task_class = globals()[f'{request}RequestsHost']
    task_class.endpoint = endpoint
    execute_locust_tasks(context, [task_class_name])



