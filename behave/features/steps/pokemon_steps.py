from behave import given, when, then
import requests

@given('Small talk')
def small_talk(context):
    print('Greetings')
    
@when('Hi')
def hi(context):
    print('Hi hi')

@then('Bye')
def bye(context):
    print('Bye Bye')


@given('I have a RESTful API "{endpoint}"')
def specify_api_endpoint(context, endpoint):
    context.endpoint = endpoint
    
@when('I make a GET request for "{pokemon}" data')
def make_get_request(context, pokemon):
    url = f'{context.endpoint}{pokemon}'
    print(url)
    context.req = requests.get(url)
    
@then('the response should be "{status_result}"')
def verify_request_status_code(context, status_result):
    print(f'STATUS CODE: {context.req.status_code}')
    print(f'STATUS result: {status_result}')
    assert int(status_result) == context.req.status_code
