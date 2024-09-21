from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from features.locators.MovieDetailLocators import user_dropdown_section, history_user_dropdown_option, \
    current_movie_text, add_to_history_button, all_plays_button, added_to_history_button
from features.pages.BasePage import BasePage

class MovieDetailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_add_to_history_button(self):
        self.click(add_to_history_button)

    def click_all_plays_button(self):
        self.click(all_plays_button)

    def hover_user_dropdown_button(self):
        self.hover_and_wait_for_click(user_dropdown_section, history_user_dropdown_option)
        sleep(5)

    def click_history_button(self):
        pass

    def get_movie_title(self):
        full_movie_title = self.get_text(current_movie_text)
        just_title = full_movie_title.rsplit(' ', 1)[0]
        print(just_title, "Movie Title from Movie detail page")
        return just_title

    def click_history_added_button(self):
         self.click(added_to_history_button)

