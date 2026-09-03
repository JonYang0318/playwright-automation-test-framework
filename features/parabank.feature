Feature: ParaBank customer workflows
  As a ParaBank customer
  I want to use the banking portal
  So that I can verify the main customer journeys

  @smoke @login
  Scenario: A customer can log in and log out
    Given I open the ParaBank home page
    When I log in with username "john" and password "demo"
    Then I should see the Accounts Overview page
    When I log out
    Then I should see the Customer Login form

  @smoke
  Scenario: The login form is available
    Given I open the ParaBank home page
    Then the login form should be ready

  @negative
  Scenario: Invalid credentials are rejected
    Given I open the ParaBank home page
    When I log in with username "invalid-user" and password "invalid-password"
    Then I should see the invalid login message

  @functional
  Scenario: A customer can view the account overview
    Given I am logged in to ParaBank
    Then the account overview should show Account and Balance columns

  @functional
  Scenario: A customer can open the new account form
    Given I am logged in to ParaBank
    When I open the new account page
    Then the new account form should be visible

  @functional
  Scenario: A customer can search transactions
    Given I am logged in to ParaBank
    When I open the transaction search page
    And I search transactions by account
    Then the transaction search page should remain available

  @functional
  Scenario: A customer can open the update contact page
    Given I am logged in to ParaBank
    When I open the update contact information page
    Then the update profile page should be visible
