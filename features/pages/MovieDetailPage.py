from features.locators.MovieDetailLocators import user_dropdown_section, history_user_dropdown_option, \
    current_movie_text, add_to_history_button, not_yet_add_to_history_button, all_plays_button
from features.pages.BasePage import BasePage

class MovieDetailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_add_to_history_button(self):
        self.click(add_to_history_button)

    def click_remove_from_history_button(self):
        self.click(not_yet_add_to_history_button)

    def click_all_plays_button(self):
        self.click(all_plays_button)

    def hover_user_dropdown_button(self):
        self.hover_over_element(user_dropdown_section)

    def click_history_button(self):
        self.click(history_user_dropdown_option)

    def get_movie_title(self):
        full_movie_title = self.get_text(current_movie_text)
        just_title = full_movie_title.rsplit(' ', 1)[0]
        print(just_title, "Movie Title from Movie detail page")
        return just_title



