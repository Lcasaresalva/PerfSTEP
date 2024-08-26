import gevent

from locust import events
from locust.env import Environment

from locust.stats import stats_history, stats_printer
from locust.log import setup_logging

from tasks.actions_resources import ActionsOnResources
from tasks.actions_users import ActionsOnUsers
from executions.endurance_example import ThreadGroupForUsers, ThreadGroupForAdmins
from executions.request_endpoint import *


def execute_locust_tasks(context, task_classes_name):
    setup_logging("DEBUG")

    task_classes = [globals()[task_class_name] for task_class_name in task_classes_name]

    context.env = Environment(user_classes=task_classes, events=events, host=context.host)

    runner = context.env.create_local_runner()
    # runner = env.create_master_runner("*", 5572)

    # execute init event handlers (only really needed if you have registered any)
    context.env.events.init.fire(environment=context.env, runner=runner)

    # start a greenlet that periodically outputs the current stats
    gevent.spawn(stats_printer(context.env.stats))

    # start a greenlet that save current stats to history
    gevent.spawn(stats_history, context.env.runner)

    # start the test
    runner.start(context.users, spawn_rate=context.spawn_rate)

    # stop the test after test_time
    gevent.spawn_later(context.test_time, runner.quit)

    # wait for the greenlets
    runner.greenlet.join()


