Feature: Cancel Payment

  @regression @cancel
  Scenario: Cancel a payment before capture
    Given I have stored "payment_id"
    When I send a "POST" request to "/payments/{payment_id}/cancel"
    Then the response status code should be 200 or 201