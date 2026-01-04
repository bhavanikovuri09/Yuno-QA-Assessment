Feature: Edge cases forcing errors (test cards)

  @negative @cards
  Scenario: Payment declined - insufficient funds
    Given I load request payload "testdata/payment_min.json"
    And I set "workflow" to "DIRECT"
    And I apply card fixture "testdata/card_insufficient_funds.json"
    When I send a "POST" request to "/payments" with the loaded payload
    Then the response status code should be 400 or 422

  @negative @cards
  Scenario: Payment declined - invalid security code (CVV)
    Given I load request payload "testdata/payment_min.json"
    And I set "workflow" to "DIRECT"
    And I apply card fixture "testdata/card_invalid_cvv.json"
    When I send a "POST" request to "/payments" with the loaded payload
    Then the response status code should be 400 or 422