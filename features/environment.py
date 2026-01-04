import json
from utils.api_client import ApiClient

def before_all(context):
    # One API client for entire test run
    context.api = ApiClient()
    context.vars = {}

def before_scenario(context, scenario):
    # Clear previous scenario data
    context.last_response = None
    context.last_json = None
    context.vars.clear()

def after_step(context, step):
    "If the last_response exists, try to parse JSON to last_json.This keeps step definitions simple."
    if getattr(context, "last_response", None) is None:
        return

    try:
        context.last_json = context.last_response.json()
    except Exception:
        context.last_json = None

def pretty_response(response) -> str:
    try:
        return json.dumps(response.json(), indent=2)
    except Exception:
        return response.text
