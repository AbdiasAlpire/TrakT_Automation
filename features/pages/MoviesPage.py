from features.locators.MoviesLocators import movie_locator
from features.pages.BasePage import BasePage

class MoviesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_a_movie(self):
        self.click(movie_locator)