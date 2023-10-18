# Created by white at 10/15/2023
Feature: Settings Tests

  Scenario: User can access Whatsapp and Telegram communities
    Given Open Off Plan page
    When Signin
    And Click on settings option
    And Store original window
    And Click on support option
    And Switch to new window
    Then Verify support page opens
    And Close page
    And Return to original window
    When Click on news option
    Then Verify news page opens

