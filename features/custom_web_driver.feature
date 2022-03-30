Feature: Custom Web Driver

    Create a custom web driver including these features:
    - Check if the web driver is available

    Scenario: Check if the web driver is available
        Given I have a custom web driver
        Then I should see the web driver is available
        When I make the web driver quit
        Then I should see the web driver is not available