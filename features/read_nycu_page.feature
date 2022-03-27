Feature: selenium controll
	Scenario: Open NYCU home page
		Given a chrome driver launched
		And test step loaded
		When I open the NYCU home page
		Then I should see correct title
			| title                 |
			| NYCU 國立陽明交通大學 |
		When I maximize the browser
		Then browser should be maximized
		When I click on the nav item
		Then I should see the correct page
			| title                          |
			| 新聞網 – NYCU 國立陽明交通大學 |
		When I click on the first news in the page
		Then driver should print the title and content
	Scenario: Open new tab and switch to it
		Given a chrome driver launched
		When after the news is printed
		Then open a new tab and switch to it
		And navigate to google
		When I input student number and submit
		Then driver should print the title of second result
		And close the browser
