from io import StringIO
from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.web_test import WebTest


@fixture
def driver_setup(context):
    context.web_test = WebTest()
    webdriver_service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=webdriver_service)
    yield context.driver
    context.driver.quit()
    context.web_test.driver_quit()


@fixture
def strio_setup(context):
    context.strio = StringIO()
    return context.strio


def before_all(context):
    use_fixture(driver_setup, context)
    use_fixture(strio_setup, context)
