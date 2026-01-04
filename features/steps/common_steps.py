import json
import os
from behave import given, when, then


def _read_json(file_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def _substitute_vars(context, text: str) -> str:
    """
    Replaces placeholders like {payment_id} with values stored in context.vars
    """
    if not hasattr(context, "vars") or context.vars is None:
        return text

    for k, v in context.vars.items():
        text = text.replace("{" + k + "}", str(v))
    return text


@given('I load request payload "{file_path}"')
def step_load_payload(context, file_path):
    context.payload = _read_json(file_path)


@given('I set "{key}" to "{value}"')
def step_set_field(context, key, value):
    if not hasattr(context, "payload") or context.payload is None:
        context.payload = {}

    # keep as string (good for BDD); API may still accept boolean-like strings
    context.payload[key] = value


@given('I have stored "{key}"')
def step_have_var(context, key):
    assert hasattr(context, "vars") and context.vars is not None, "context.vars not initialized"
    assert key in context.vars and context.vars[key], f"Missing context var: {key}"


@given('I have stored "{key1}" and "{key2}"')
def step_have_two_vars(context, key1, key2):
    assert hasattr(context, "vars") and context.vars is not None, "context.vars not initialized"
    assert key1 in context.vars and context.vars[key1], f"Missing context var: {key1}"
    assert key2 in context.vars and context.vars[key2], f"Missing context var: {key2}"


@when('I send a "{method}" request to "{path}" with the loaded payload')
def step_send_request_with_body(context, method, path):
    final_path = _substitute_vars(context, path)
    context.last_response = context.api.request(method, final_path, payload=context.payload)


@when('I send a "{method}" request to "{path}"')
def step_send_request_no_body(context, method, path):
    final_path = _substitute_vars(context, path)
    context.last_response = context.api.request(method, final_path, payload=None)


@then("the response status code should be 200 or 201")
def step_status_200_201(context):
    assert context.last_response is not None, "No response captured."
    assert context.last_response.status_code in (200, 201), (
        f"Expected 200/201 but got {context.last_response.status_code}. "
        f"Body: {context.last_response.text}"
    )


@then("the response status code should be 400 or 422")
def step_status_400_422(context):
    assert context.last_response is not None, "No response captured."
    assert context.last_response.status_code in (400, 422), (
        f"Expected 400/422 but got {context.last_response.status_code}. "
        f"Body: {context.last_response.text}"
    )


@then('the response should contain a non-empty field "{field}"')
def step_response_has_field(context, field):
    assert context.last_json is not None, f"Response is not JSON. Body: {context.last_response.text}"
    assert field in context.last_json, f"Field '{field}' not found in response JSON: {context.last_json}"
    assert str(context.last_json[field]).strip() != "", f"Field '{field}' is empty"

    # store commonly used ids for later steps
    if field == "id":
        context.vars["payment_id"] = context.last_json[field]

    # best-effort: if the response contains transaction_id, store it too
    if field in ("transaction_id", "transactionId"):
        context.vars["transaction_id"] = context.last_json[field]


@then('I store "{field}" as "{var_name}"')
def step_store_field_as_var(context, field, var_name):
    """
    Optional helper:
    - Lets feature files store any response field into context.vars.
    Example: Then I store "transaction_id" as "transaction_id"
    """
    assert context.last_json is not None, f"Response is not JSON. Body: {context.last_response.text}"
    assert field in context.last_json, f"Field '{field}' not found in response JSON: {context.last_json}"
    context.vars[var_name] = context.last_json[field]

@given('I apply card fixture "{file_path}"')
def step_apply_card_fixture(context, file_path):
    card_data = _read_json(file_path)

    if not hasattr(context, "payload") or context.payload is None:
        context.payload = {}

    # Best-effort placement for common Yuno payment payload structures.
    # If your payload uses different nesting, adjust these keys.
    pm = context.payload.setdefault("payment_method", {})
    detail = pm.setdefault("detail", {})
    card = detail.setdefault("card", {})
    card.update(card_data)    