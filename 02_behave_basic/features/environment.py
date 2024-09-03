from behave.configuration import Configuration


def before_all(context):
    print('Actions before all')


def before_feature(context, feature):
    print('Actions before feature')


def before_scenario(context, scenario):
    print('Actions before scenario')


def after_scenario(context, scenario):
    print('Actions after scenario')


def after_feature(context, feature):
    print('Actions after feature')



