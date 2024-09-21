from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
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
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
            return element.text
        except TimeoutException:
            return "Error: Element not found."

    def is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except:
            return False

    def select_from_dropdown(self, by_locator, value):
        select = Select(WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)))
        select.select_by_value(value)

    def wait_for_element(self, by_locator):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))

    def get_title(self):
        return self.driver.title

    def is_present(self, by_locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(by_locator)
            )
            return element.is_displayed() and element.is_enabled()
        except (TimeoutException, NoSuchElementException):
            return False

    def get_current_url(self):
        return self.driver.current_url

    def hover_over_element(self, by_locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def hover_and_wait_for_click(self, hover_locator, click_locator):
        hover_element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(hover_locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element).perform()
        clickable_element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(click_locator)
        )
        clickable_element.click()

    def search_text_on_page(self, by_locator):
        text_to_search = self.get_text(by_locator)
        page_source = self.driver.page_source
        if text_to_search in page_source:
            return True
        else:
            return False

    def scroll_until_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(by_locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(by_locator)
            ).click()
        except TimeoutException:
            print(f"Could not find or click the element {by_locator}")
            self.driver.save_screenshot("scroll_and_click_failure.png")
            raise

    def scroll_to_middle(self):
        scroll_script = "window.scrollTo(0, document.body.scrollHeight / 2);"
        self.driver.execute_script(scroll_script)

    def scroll_and_click(self, by_locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(by_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(by_locator)
        ).click()