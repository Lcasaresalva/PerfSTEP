import sys

import gevent
import greenlet

from locust import events
from locust.env import Environment

from locust.stats import stats_history, stats_printer
from locust.log import setup_logging

from executions.endurance_example import *
from executions.request_endpoint import *


def execute_locust_tasks(context, task_classes_name):
    setup_logging("DEBUG")

    task_classes = [globals()[task_class_name] for task_class_name in task_classes_name]
    from urllib3 import HTTPConnectionPool
    pool = HTTPConnectionPool(context.host)
    # context.env = Environment(user_classes=task_classes, events=events, host=context.host)
    context.env = Environment(user_classes=task_classes, host=context.host)
    context.env.stop_timeout = 20
    runner = context.env.create_local_runner()
    # runner = env.create_master_runner("*", 5572)

    # # execute init event handlers (only really needed if you have registered any)
    # context.env.events.init.fire(environment=context.env, runner=runner)

    # start a greenlet that periodically outputs the current stats
    gevent.spawn(stats_printer(context.env.stats))
    #
    # start a greenlet that save current stats to history
    gevent.spawn(stats_history, context.env.runner)

    # start the test
    runner.start(context.users, spawn_rate=context.spawn_rate)
    # import pdb
    # import sys
    # pdb.Pdb(stdout=sys.__stdout__).set_trace()
    # import time
    # time.sleep(context.spawn_rate)
    # gevent.spawn(lambda: runner.quit())

    # stop the test after test_time
    gevent.spawn_later(context.test_time, runner.quit)

    # wait for the greenlets
    # runner.greenlet.kill()
    runner.greenlet.join()
    # runner.greenlet.
    # runner.greenlet.kill()
    # runner.stop()
    # runner.stop_users(runner.user_classes_count)
    # runner.quit()
    import pdb
    import sys
    pdb.Pdb(stdout=sys.__stdout__).set_trace()
    context.env.stats.reset_all()


    pool.close()
    # gevent.killall(runner.greenlet, block=False, timeout=10)



    # context.env.events.test_stop()


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("Stopped test from Master node")