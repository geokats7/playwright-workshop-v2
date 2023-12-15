from page_objects.login_page import LoginPage
import os


def test_login_successful(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    login_page = LoginPage(page)
    login_page.fill_username(os.getenv("LOGIN_USERNAME"))
    login_page.fill_password(os.getenv("LOGIN_PASSWORD"))
    login_page.click_submit()
    assert login_page.element_is_visible(login_page.SUCCESSFUL_LOGIN_TEXT)



def test_login_wrong_username(page):
    # Refactor this test to use the page objects pattern
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.locator("#username").fill("wrong_username")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()
    assert page.locator("#error").inner_text() == "Your username is invalid!"