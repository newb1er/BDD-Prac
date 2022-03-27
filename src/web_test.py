from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class WebTestStep(ABC):

    def __init__(self, url):
        self.url = url
        self.driver = None

    def navigate(self):
        self.driver.get(self.url)

    @abstractmethod
    def post_action(self):
        return NotImplemented

    @abstractmethod
    def action(self):
        return NotImplemented


class NYCUTestStep(WebTestStep):

    def __init__(self):
        url = 'https://www.nycu.edu.tw/'
        super().__init__(url)

    def maximize_window(self):
        self.driver.maximize_window()

    def click_nav_item(self):
        self.driver.find_element(By.LINK_TEXT, '消息').click()

    def click_first_new(self):
        list_item = self.driver.find_element(By.ID, '-tab').find_element(
            By.TAG_NAME, 'li')
        list_item.find_element(By.TAG_NAME, 'a').click()

        title = self.driver.find_element(By.CLASS_NAME, 'entry-title').text
        content = self.driver.find_element(By.CLASS_NAME, 'entry-content').text

        print(f'{title}\n{content}')

    def post_action(self):
        pass

    def action(self):
        self.maximize_window()
        self.click_nav_item()
        self.click_first_new()


class GoogleTestStep(WebTestStep):

    def __init__(self):
        url = 'https://www.google.com'
        super().__init__(url)

    def post_action(self):
        pass

    def action(self):
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
        test_step.driver = self.driver

    def do_post_action(self):
        self.test_step.post_action()

    def do_navigate(self):
        self.test_step.navigate()

    def do_action(self):
        self.test_step.action()
