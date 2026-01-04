Feature: Payments API - Authorization

  @regression @authorization
  Scenario: Authorize payment without capture
    Given I load request payload "testdata/payment_min.json"
    And I set "workflow" to "DIRECT"
    And I set "capture" to "false"
    When I send a "POST" request to "/payments" with the loaded payload
    Then the response status code should be 200 or 201
