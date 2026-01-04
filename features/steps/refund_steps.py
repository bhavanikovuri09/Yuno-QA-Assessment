from behave import when, then

@when('I refund the payment fully')
def step_refund_full(context):
    payment_id = context.vars.get("payment_id")
    assert payment_id, "payment_id not found in context"

    context.last_response = context.api.post(
        f"/payments/{payment_id}/refund"
    )
    try:
        context.last_json = context.last_response.json()
    except Exception:
        context.last_json = None


@when('I refund the payment partially with amount "{amount}"')
def step_refund_partial(context, amount):
    payment_id = context.vars.get("payment_id")
    assert payment_id, "payment_id not found in context"

    payload = {
        "amount": int(amount)
    }

    context.last_response = context.api.post(
        f"/payments/{payment_id}/refund",
        payload=payload
    )
    try:
        context.last_json = context.last_response.json()
    except Exception:
        context.last_json = None


@then('the refund status should be "{status}"')
def step_validate_refund_status(context, status):
    assert context.last_json is not None, "Response JSON is empty"
    assert context.last_json.get("status") == status, (
        f"Expected refund status '{status}', got '{context.last_json.get('status')}'"
    )
