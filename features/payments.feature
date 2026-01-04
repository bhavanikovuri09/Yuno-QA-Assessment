Feature: Payments API - Create Payment

  @sanity @payments
  Scenario: Create payment with minimal payload (DIRECT workflow)
    Given I load request payload "testdata/payment_min.json"
    And I set "workflow" to "DIRECT"
    When I send a "POST" request to "/payments" with the loaded payload
    Then the response status code should be 200 or 201
    And the response should contain a non-empty field "id"

  @regression @payments
  Scenario: Create payment with maximal payload (DIRECT workflow)
    Given I load request payload "testdata/payment_max.json"
    And I set "workflow" to "DIRECT"
    When I send a "POST" request to "/payments" with the loaded payload
    Then the response status code should be 200 or 201
    And the response should contain a non-empty field "id"

  @negative @payments
  Scenario: Create payment fails when workflow is not DIRECT
    Given I load request payload "testdata/payment_min.json"
    And I set "workflow" to "REDIRECT"
    When I send a "POST" request to "/payments" with the loaded payload
    Then the response status code should be 400 or 422