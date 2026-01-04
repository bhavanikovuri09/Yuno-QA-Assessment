Feature: Capture Authorization

  @regression @capture
  Scenario: Capture a previously authorized payment
    Given I have stored "payment_id" and "transaction_id"
    When I send a "POST" request to "/payments/{payment_id}/transactions/{transaction_id}/capture"
    Then the response status code should be 200 or 201