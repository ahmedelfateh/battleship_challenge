from behave import *
import requests


@given('a shot at {x},{y}')
def step_impl(context, x, y):
    payload = {
        'x': int(x),
        'y': int(y),
    }
    context.response = context.session.put(
        context.request_url,
        json=payload
    )
