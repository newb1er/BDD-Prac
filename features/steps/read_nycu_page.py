from selenium.webdriver.common.by import By

from src.web_test import NYCUTestStep


@given('a chrome driver launched')
def step_impl(context):
    print(context.web_test.driver.title)


@then('link to NYCU home page')
def step_impl(context):
    context.web_test.load_test_step(NYCUTestStep())
    context.web_test.do_navigate()
    context.driver.get('https://www.nycu.edu.tw/')

    assert context.web_test.driver.title == context.driver.title


@then('The driver window should be maximized')
def step_impl(context):
    context.web_test.do_action()
    context.driver.maximize_window()

    print(f'web_test_step: {context.web_test.test_step.url}')
    print(f'web_test: {context.web_test.driver.get_window_size()}')
    print(f'driver: {context.driver.get_window_size()}')

    assert context.web_test.driver.get_window_size(
    ) == context.driver.get_window_size()


@then('the "消息" nav item should be clicked')
def step_impl(context):
    assert context.web_test.driver.current_url == 'https://www.nycu.edu.tw/news-network/'


@then('navigate to the first news in the page')
def step_impl(context):
    context.driver.get('https://www.nycu.edu.tw/news-network/')
    list_item = context.driver.find_element(By.ID, '-tab').find_element(
        By.TAG_NAME, 'li')
    list_item.find_element(By.TAG_NAME, 'a').click()

    assert context.web_test.driver.current_url == context.driver.current_url
