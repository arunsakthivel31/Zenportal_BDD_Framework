Feature: Zen Portal Login

  Scenario: Successful Login
    Given User opens Zen Portal
    When User enters valid username and password
    And User clicks login button
    Then Login should be successful

  Scenario: Unsuccessful Login
    Given User opens Zen Portal
    When User enters invalid username and password
    And User clicks login button
    Then Login should fail

  Scenario: Validate Username Input Box
    Given User opens Zen Portal
    Then Username textbox should be displayed

  Scenario: Validate Password Input Box
    Given User opens Zen Portal
    Then Password textbox should be displayed

  Scenario: Validate Submit Button
    Given User opens Zen Portal
    Then Login button should be enabled

  Scenario: Validate Logout
    Given User logged into portal
    When User clicks logout
    Then User should logout successfully