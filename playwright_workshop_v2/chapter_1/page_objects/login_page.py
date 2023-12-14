from page_objects.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = "#username"
    PASSWORD_FIELD = "#password"
    SUBMIT_BUTTON = "#submit"
    SUCCESSFUL_LOGIN_TEXT = "text=Logged In Successfully"

    def fill_username(self, username):
        # page.locator(self.USERNAME_FIELD).fill(username)
        self.send_keys(self.USERNAME_FIELD, username)

    def fill_password(self, password):
        # page.locator(self.PASSWORD_FIELD).fill(password)
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_submit(self):
        # page.locator(self.SUBMIT_BUTTON).click()
        self.click(self.SUBMIT_BUTTON)