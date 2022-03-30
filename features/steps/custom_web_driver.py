from behave import given, when, then


@given('I have a custom web driver')
def step_impl(context):
    assert context.driver is not None


@then('I should see the web driver is available')
def step_impl(context):
    assert context.driver.available


@when('I make the web driver quit')
def step_impl(context):
    context.driver.quit()


@then('I should see the web driver is not available')
def step_impl(context):
    assert not context.driver.available
