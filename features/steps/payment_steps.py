from behave import when, then
import json

@when('I create a payment')
def step_create_payment(context):
    context.last_response = context.api.post(
        "/payments",
        payload=context.payload
    )
    try:
        context.last_json = context.last_response.json()
    except Exception:
        context.last_json = None


@when('I authorize a payment')
def step_authorize_payment(context):
    payment_id = context.vars.get("payment_id")
    assert payment_id, "payment_id not found in context"

    context.last_response = context.api.post(
        f"/payments/{payment_id}/authorize"
    )
    try:
        context.last_json = context.last_response.json()
    except Exception:
        context.last_json = None


@then('the payment status should be "{status}"')
def step_validate_payment_status(context, status):
    assert context.last_json is not None, "Response JSON is empty"
    assert context.last_json.get("status") == status, (
        f"Expected status '{status}', got '{context.last_json.get('status')}'"
    )
