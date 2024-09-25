
import gevent
import os

from locust.stats import StatsCSVFileWriter
from locust import events
from locust.env import Environment

from locust.stats import stats_history, stats_printer, get_percentile_stats_summary
from locust.log import setup_logging

from executions.load_example import *
from executions.request_endpoint import *


def execute_locust_tasks(context, task_classes_name):
    setup_logging("DEBUG")

    task_classes = [globals()[task_class_name] for task_class_name in task_classes_name]

    context.env = Environment(user_classes=task_classes, events=events, host=context.host)

    runner = context.env.create_local_runner()

    # execute init event handlers (only really needed if you have registered any)
    context.env.events.init.fire(environment=context.env, runner=runner)

    # start a greenlet that periodically outputs the current stats
    gevent.spawn(stats_printer(context.env.stats))

    # start a greenlet that save current stats to history
    gevent.spawn(stats_history, context.env.runner)

    # start the test
    runner.start(context.users, spawn_rate=context.spawn_rate)

    # stop the test after test_time
    gevent.spawn_later(context.test_time, runner.stop)

    # wait for the greenlets
    runner.greenlet.join(timeout=20)
    context.env.stats.clear_all()

