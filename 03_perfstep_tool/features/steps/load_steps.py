from behave import step

from execution_lib import execute_locust_tasks
from executions.load_example import ThreadGroupForUsers, ThreadGroupForAdmins


@step('{users:d} users accessed with the proper profile every {spawn_rate:d} seconds')
def step1(context, users, spawn_rate):
    context.users = users
    context.spawn_rate = spawn_rate


@step('the scenario should take "{test_time:d}" seconds')
def step1(context, test_time):
    context.test_time = test_time


@step('I configure the following tasks with weights')
def step2(context):
    context.task_class_name = [row['task'] for row in context.table]
    context.task_class_weight = [row['weight'] for row in context.table]


@step('I execute the load scenario')
def execute_locust_task(context):

    tasks_class_name = context.task_class_name

    task_classes = [globals()[task_class_name] for task_class_name in tasks_class_name]
    weight_list = context.task_class_weight

    for i in range(0, len(task_classes)):
        task_classes[i].weight = int(weight_list[i])

    execute_locust_tasks(context, tasks_class_name)


@step('I check performance results according to')
def check_results(context):
    context.nfr_list = [row['nfr'] for row in context.table]
    context.criteria_list = [row['criteria'] for row in context.table]
    perf_nfr = dict(zip(context.nfr_list, context.criteria_list))
    print(perf_nfr)

    environment = context.env

    failed_criteria = ''

    if environment.stats.total.get_response_time_percentile(0.95) > int(perf_nfr['95%']):
        failed_criteria += f' - 95th percentile response time > 100 ms: {environment.stats.total.get_response_time_percentile(0.95)} ms'
    if environment.stats.total.avg_response_time > int(perf_nfr['avgRT']):
        failed_criteria += f' - Average response time ratio > 150 ms: {environment.stats.total.avg_response_time} ms'
    if environment.stats.total.fail_ratio >= float(perf_nfr['ratio']):
        failed_criteria += f' - Error ratio exceeds 5%: {environment.stats.total.fail_ratio}'

    print('NFRs fully met!') if failed_criteria == '' else print(f'NFRs failed during this run: \n {failed_criteria}')
    assert failed_criteria == '', f'NFRs failed during this run:\n {failed_criteria}'
