from features.locators.MovieDetailLocators import user_dropdown_section, history_user_dropdown_option, \
    current_movie_text, add_to_history_button, all_plays_button, added_to_history_button, add_comment_button, \
    movie_comment_input, comment_posted_button, submit_button
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

    def click_history_button(self):
        pass

    def get_movie_title(self):
        full_movie_title = self.get_text(current_movie_text)
        just_title = full_movie_title.rsplit(' ', 1)[0]
        print(just_title, "Movie Title from Movie detail page")
        return just_title

    def click_history_added_button(self):
         self.click(added_to_history_button)

    def click_add_comment_button(self):
        self.click(add_comment_button)

    def fill_movie_comment_input(self, movie_comment):
        self.send_keys(movie_comment_input, movie_comment)

    def is_comment_posted(self):
        return self.is_visible(comment_posted_button)

    def click_submit_comment_button(self):
        self.click(submit_button)


