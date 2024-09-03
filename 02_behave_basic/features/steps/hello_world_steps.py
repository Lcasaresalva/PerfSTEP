from behave import step


@step('I print hello world')
def step1(context):
    print('TEST LOG: Hello world')

