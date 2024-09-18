from features.locators.DashboardLocators import movies_header_link_locator
from features.locators.MoviesLocators import movie_locator
from features.pages.BasePage import BasePage

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_username_visible(self, username_text):
        return self.is_visible(username_text)

    def am_i_in_dashboard(self):
        return self.get_current_url()

    def click_movies_link(self):
        self.click(movies_header_link_locator)
