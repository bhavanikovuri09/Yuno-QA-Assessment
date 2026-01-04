# Manual Test Cases – Payment APIs

## Scope
This document covers manual test scenarios for Payment APIs including Purchase, Authorization, Capture, Cancel, Refund, and Verify flows. Negative and edge cases are included.

---

## Purchase / Payment

| Test Case ID | Scenario | Type | Priority |
|-------------|---------|------|---------|
| TC_PAY_001 | Create payment with minimal fields | Positive | Sanity |
| TC_PAY_002 | Create payment with maximal fields | Positive | Regression |
| TC_PAY_003 | Invalid card number | Negative | Regression |
| TC_PAY_004 | Insufficient funds | Negative | Regression |

---

## Authorization

| Test Case ID | Scenario | Type | Priority |
|-------------|---------|------|---------|
| TC_AUTH_001 | Authorize payment (minimal) | Positive | Sanity |
| TC_AUTH_002 | Authorize payment (maximal) | Positive | Regression |
| TC_AUTH_003 | Expired card | Negative | Regression |

---

## Capture

| Test Case ID | Scenario | Type | Priority |
|-------------|---------|------|---------|
| TC_CAP_001 | Capture authorized payment | Positive | Sanity |
| TC_CAP_002 | Capture already captured payment | Negative | Regression |

---

## Cancel

| Test Case ID | Scenario | Type | Priority |
|-------------|---------|------|---------|
| TC_CAN_001 | Cancel authorized payment | Positive | Sanity |
| TC_CAN_002 | Cancel captured payment | Negative | Regression |

---

## Refund

| Test Case ID | Scenario | Type | Priority |
|-------------|---------|------|---------|
| TC_REF_001 | Full refund | Positive | Sanity |
| TC_REF_002 | Partial refund | Positive | Regression |
| TC_REF_003 | Refund without capture | Negative | Regression |

---

## Verify

| Test Case ID | Scenario | Type | Priority |
|-------------|---------|------|---------|
| TC_VER_001 | Verify card with valid details | Positive | Sanity |
| TC_VER_002 | Verify card with invalid CVV | Negative | Regression |

---

## Non-Functional Scenarios
- API response time validation
- Error message clarity
- Data consistency across flows
- Security validation (masking, encryption)
