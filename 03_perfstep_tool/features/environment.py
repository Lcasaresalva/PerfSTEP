from behave.configuration import Configuration


def before_scenario(context, scenario):
    conf = Configuration()
    context.host = conf.userdata["host"]


def after_scenario(context, scenario):
    context.env.stats.clear_all()

