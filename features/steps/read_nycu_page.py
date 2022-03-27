from behave import given, when, then
from behave.log_capture import capture
from selenium.webdriver.common.by import By
import sys

from src.web_test import NYCUTestStep


@given('a chrome driver launched')
def step_impl(context):
    print(context.web_test.driver.title)


@given('test step loaded')
def step_impl(context):
    context.web_test.load_test_step(NYCUTestStep())


@when('I open the NYCU home page')
def step_impl(context):
    context.web_test.do_navigate()


@then('I should see correct title')
def step_impl(context):
    context.web_test.driver.title == context.table[0]['title']


@when('I maximize the browser')
def step_impl(context):
    context.web_test.test_step.maximize_window()


@then('browser should be maximized')
def step_impl(context):
    context.driver.maximize_window()

    assert context.web_test.driver.get_window_size(
    ) == context.driver.get_window_size()


@when('I click on the nav item')
def step_impl(context):
    context.web_test.test_step.click_nav_item()


@then('I should see the correct page')
def step_impl(context):
    context.web_test.driver.title == context.table[0]['title']


@when('I click on the first news in the page')
def step_impl(context):
    origin_stdout = sys.stdout
    sys.stdout = context.strio
    context.web_test.test_step.click_first_new()
    sys.stdout = origin_stdout


@capture
@then('driver should print the title and content')
def step_impl(context):
    context.driver.get('https://www.nycu.edu.tw/news-network/')
    context.driver.find_element(By.ID, '-tab').find_element(
        By.TAG_NAME, 'li').find_element(By.TAG_NAME, 'a').click()
    title = context.driver.find_element(By.CLASS_NAME, 'entry-title').text
    content = context.driver.find_element(By.CLASS_NAME, 'entry-content').text

    assert context.strio.getvalue() == f'{title}\n{content}\n'
