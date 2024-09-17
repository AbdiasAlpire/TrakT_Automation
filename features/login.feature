Feature: Login functionality
  @login
  Scenario: Login using valid credentials
    Given I got navigated to trakt Login page
    When I enter a valid Email
    And I enter a a valid password
    And I click on Sing in icon
    And I click on Exit button
    Then I should be able to see my username on dashboard