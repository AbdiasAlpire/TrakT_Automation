from features.locators.LoginLocators import email_input_locator, password_input_locator, login_button_locator
from features.pages.BasePage import BasePage


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_username_visible(self, username_text):
        self.is_visible(username_text)
