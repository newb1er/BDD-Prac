Feature: selenium controll
	Scenario: Open NYCU home page
		Given a chrome driver launched
		Then link to NYCU home page
		And The driver window should be maximized
		And the '消息' nav item should be clicked
		And navigate to the first news in the page
		And It should print the title and content of the news 
	Scenario: Open new tab and switch to it
		Given a chrome driver launched 
		When after the news is printed
		Then open a new tab and switch to it
		And navigate to google
		And input student number and submit
		And print the title of second result
		And close the browser
