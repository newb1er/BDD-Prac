from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class WebTestStep(ABC):

    def __init__(self, url):
        self.url = url

    def navigate(self, driver):
        driver.get(self.url)

    @abstractmethod
    def action(self, driver):
        return NotImplemented


class NYCUTestStep(WebTestStep):

    def __init__(self):
        url = 'https://www.nycu.edu.tw/'
        super().__init__(url)

    def action(self, driver):
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, '消息').click()
        list_item = driver.find_element(By.ID, '-tab').find_element(
            By.TAG_NAME, 'li')
        list_item.find_element(By.TAG_NAME, 'a').click()


class GoogleTestStep(WebTestStep):

    def __init__(self):
        url = 'https://www.google.com'
        super().__init__(url)

    def action(self, driver):
        pass


class WebTest:

    def __init__(self):
        self.test_step = None
        webdriver_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=webdriver_service)

    def driver_quit(self):
        self.driver.quit()

    def load_test_step(self, test_step):
        self.test_step = test_step

    def do_navigate(self):
        self.test_step.navigate(self.driver)

    def do_action(self):
        self.test_step.action(self.driver)
