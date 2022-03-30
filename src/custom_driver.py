from webbrowser import get
from selenium import webdriver


class CustomChrome(webdriver.Chrome):

    @property
    def available(self):
        return self.session_id is not None

    def quit(self):
        super().quit()
        print('hi')
        self.session_id = None