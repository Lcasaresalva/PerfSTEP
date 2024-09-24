from behave import step
import json
from behave.configuration import Configuration
from executions.request_endpoint import *
from execution_lib import execute_locust_tasks


@step('the request body is')
def step1(context):
    context.body = json.loads(context.text)


@step('I use the {user} user')
def step1(context, user):
    conf = Configuration()
    context.headers = {'accept': 'application/json', 'api_key': conf.userdata[f"user_{user}_key"]}


@step('I execute the "{request}" to "{endpoint}" endpoint')
def execute_locust_task(context, request, endpoint):

    context.host = "http://localhost:8080/api/v3"
    task_class_name = f'{request}RequestsHost'
    task_class = globals()[f'{request}RequestsHost']
    task_class.endpoint = endpoint
    task_class.body = context.body if "body" in context else None
    task_class.headers = context.headers if "headers" in context else {'accept': 'application/json'}
    execute_locust_tasks(context, [task_class_name])