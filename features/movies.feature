Feature: Movies functionalities

  Background:
    Given I got navigated to trakt Login page
    When I enter a valid Email
    And I enter a a valid password
    And I click on Sing in icon

  @AddMovie
  @Priority=1
  Scenario: Add a movie to history
    Given I am in the Movies page
    When I click a movie
    And I get the title of the clicked movie
    And I click Add to History button
    And I click profile dropdown
    Then I should be able to see my added movie

  @RemoveMovie
  @Priority=2
  Scenario: Remove a movie from history
    Given I am in the Movies page
    When I click a movie
    When I get the title of the clicked movie
    And I click History added button
    And I click all play's button
    And I click profile dropdown
    Then I should be able to see my removed movie