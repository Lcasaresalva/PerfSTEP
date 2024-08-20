from behave import step

from tasks.request_endpoint import *
from execution_lib import execute_locust_tasks


@step('the user is')
def step1(context):

    context.user = {"email": context.table[0]['user'],
               "password": context.table[0]['pass']}


@step('I execute the "{request}" to "{endpoint}" endpoint')
def execute_locust_task(context, request, endpoint):

    context.host = "https://reqres.in"
    task_class_name = f'{request}RequestsHost'
    task_class = globals()[f'{request}RequestsHost']
    task_class.endpoint = endpoint
    execute_locust_tasks(context, [task_class_name])



