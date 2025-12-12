Feature: Validate FB Login functionality 

  Scenario Outline: Login with multiple credentials in parallel browsers
    Given Launch both Chrome and Edge browsers in parallel
    When Open the https://www.facebook.com/ website in both browsers
    Then the login application has been opened successfully in both browsers
    And Provide the username "<username>" and password "<password>" in both browsers
    And Click on the login button in both browsers
    Then User should be logged in successfully in both browsers
    Then Close both browsers

    Examples:
      | username              | password      |
      | test1@gmail.com       | Test@1234     |
      | test2@gmail.com       | Pass@5678     |
      | admin@example.com     | Admin@9999    |
      | user@test.com         | User@4321     |