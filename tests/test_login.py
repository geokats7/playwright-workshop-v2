def test_login_successful(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.locator("#username").fill("student")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()
    assert page.locator("text=Logged In Successfully").is_visible()

def test_login_wrong_username(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.locator("#username").fill("wrong_username")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()
    assert page.locator("#error").inner_text() == "Your username is invalid!"