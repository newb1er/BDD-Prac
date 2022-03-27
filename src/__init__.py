from src.web_test import WebTest, NYCUTestStep, GoogleTestStep


def start_test():
    web_test = WebTest()
    web_test.load_test_step(NYCUTestStep())
    web_test.do_post_action()
    web_test.do_navigate()
    web_test.do_action()
    web_test.load_test_step(GoogleTestStep())
    web_test.do_post_action()
    web_test.do_navigate()
    web_test.do_action()
    web_test.driver_quit()