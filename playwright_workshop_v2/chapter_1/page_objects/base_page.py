class BasePage:
    def __init__(self, page) -> None:
        self.page = page
    
    def click(self, locator):
        self.page.locator(locator).click()

    def send_keys(self, locator, text):
        self.page.locator(locator).fill(text)
    
    def get_text(self, locator):
        return self.page.locator(locator).inner_text()
    
    def element_is_visible(self, locator):
        return self.page.locator(locator).is_visible()