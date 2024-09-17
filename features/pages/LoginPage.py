from features.locators.LoginLocators import email_input_locator, password_input_locator, login_button_locator
from features.pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_email(self, email):
        self.send_keys(email_input_locator, email)

    def enter_password(self, password):
        self.send_keys(password_input_locator, password)

    def click_login(self):
        self.click(login_button_locator)
