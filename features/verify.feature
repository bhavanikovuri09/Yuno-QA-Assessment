Feature: Verify payment method

  As a payment system
  I want to verify a payment method
  So that card details can be validated without charging the customer


  @sanity @verify
  Scenario: Verify payment with minimal fields
    Given I load request payload "testdata/payment_min.json"
    And I set "verify" to "true"
    When I send a "POST" request to "/payments" with the loaded payload
    Then the response status code should be 200 or 201
    And the response should contain a non-empty field "id"


  @negative @verify
  Scenario: Verify payment with invalid card details
    Given I load request payload "testdata/card_invalid_cvv.json"
    And I set "verify" to "true"
    When I send a "POST" request to "/payments" with the loaded payload
    Then the response status code should be 400 or 422
