from features.locators.HistoryLocators import history_title, movie_title_on_history, alert_of_no_history
from features.locators.MovieDetailLocators import user_dropdown_section, history_user_dropdown_option, \
    current_movie_text
from features.pages.BasePage import BasePage


class HistoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_add_to_history_button(self):
        self.click_add_to_history_button()

    def click_remove_from_history_button(self):
        self.click_remove_from_history_button()

    def click_all_plays_button(self):
        self.click_all_plays_button()

    def hover_history_button(self):
        self.hover_over_element(user_dropdown_section)

    def click_history_button(self):
        self.click(history_user_dropdown_option)

    def get_movie_title_in_history(self):
        movie_title = self.get_text(movie_title_on_history)
        if movie_title == "Error: Element not found.":
            print("Movie title not found in history.")
            return None
        return movie_title

    def is_visible_no_history_alert(self):
        return self.is_visible(alert_of_no_history)