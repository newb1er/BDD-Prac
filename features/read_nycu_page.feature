Feature: selenium controll
	Scenario: Open NYCU home page
		Given a chrome driver launched
		And test step loaded
		When I open the NYCU home page
		Then I should see correct page
			| title                 |
			| NYCU 國立陽明交通大學 |
		When I maximize the browser
		Then browser should be maximized
		When I click on the nav item
		Then I should see correct page
			| title                          |
			| 新聞網 – NYCU 國立陽明交通大學 |
		When I click on the first news in the page
		Then driver should print the title and content
	Scenario: Open new tab and switch to it
		Given a chrome driver launched
		And Google Test Step is loaded
		When I open a new tab and switch to it
		And navigate to google
		Then I should see 2 tabs
		And I should see correct page
			| title  |
			| Google |
		When I input student number and submit
		Then driver should print the title of second result
		And close the browser
