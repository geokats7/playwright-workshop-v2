from page_objects.login_page import LoginPage
import os
from pytest_bdd import given, when, then, scenarios

scenarios("./features/login.feature")

@given("user navigates to Login Page")
def step_navigate_to_login(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    
    
@when("enters the correct credentials")
def step_enter_correct_credentials(page):
    login_page = LoginPage(page)
    login_page.fill_username(os.getenv("LOGIN_USERNAME"))
    login_page.fill_password(os.getenv("LOGIN_PASSWORD"))
    login_page.click_submit()


@then("user is successfully logged in")
def step_successful_login(page):
    login_page = LoginPage(page)
    assert login_page.element_is_visible(login_page.SUCCESSFUL_LOGIN_TEXT)
