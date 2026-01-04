Feature: Payments API - Refunds

  @regression @refund
  Scenario: Refund a payment
    Given I have an existing payment id
    When I send a "POST" request to "/refunds" with the loaded payload
    Then the response status code should be 200 or 201