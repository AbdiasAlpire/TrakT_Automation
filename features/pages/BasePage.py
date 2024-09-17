# features/pages/base_page.py
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def click(self, by_locator):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def select_from_dropdown(self, by_locator, value):
        select = Select(WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)))
        select.select_by_value(value)

    def wait_for_element(self, by_locator):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))

    def get_title(self):
        return self.driver.title
