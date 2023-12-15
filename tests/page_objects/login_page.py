class LoginPage:
    USERNAME_FIELD = "#username"
    PASSWORD_FIELD = "#password"
    SUBMIT_BUTTON = "#submit"

    def fill_username(self, username):
        # page.locator(self.USERNAME_FIELD).fill(username)
        send_keys(self.USERNAME_FIELD, username)

    def fill_password(self, password):
        # page.locator(self.PASSWORD_FIELD).fill(password)
        send_keys(self.PASSWORD_FIELD, password)

    def click_submit(self):
        # page.locator(self.SUBMIT_BUTTON).click()
        click(self.SUBMIT_BUTTON)