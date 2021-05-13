'''
This module contains the step definitions for duckduckgo_api.feature.
'''

import requests
from pytest_bdd import scenarios, given, then, parsers


# Constants  
DUCKDUCKGO_API = 'https://api.duckduckgo.com'

# Scenarios: 
scenarios('../features/duckduckgo_api.feature', example_converters=dict(phrase=str))

# Given Steps
@given(parsers.parse('the DuckDuckGo API is queried with "<phrase>" using "{fmt}" format'), target_fixture='ddg_response')
def ddg_response(phrase, fmt):
    params = {'q': phrase, 'format': fmt}
    response = requests.get(DUCKDUCKGO_API, params=params)
    return response

# Then steps
@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_status_code(ddg_response, code):
    assert ddg_response.status_code == code

@then(parsers.parse('the response contains results for "<phrase>"'))
def ddg_response_content(ddg_response, phrase):
    assert phrase.lower() == ddg_response.json()['Heading'].lower()
