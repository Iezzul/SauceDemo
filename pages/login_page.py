from utils.config import BASE_URL

class LoginPage:

    def __init__(self, page):
        self.page = page

    username = '[data-test="username"]'
    password = '[data-test="password"]'
    login_btn = '[data-test="login-button"]'
    error_message = '[data-test="error"]'

    def navigate(self):
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.click(self.login_btn)

    def click_login(self):
        self.page.click(self.login_btn)

    def press_enter_to_login(self, username, password):
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.locator(self.password).press("Enter")

    def get_error_message(self):
        return self.page.locator(self.error_message).text_content()

    def get_password_input_type(self):
        return self.page.locator(self.password).get_attribute("type")
