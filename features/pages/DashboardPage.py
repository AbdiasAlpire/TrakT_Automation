from features.pages.BasePage import BasePage

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_username_visible(self, username_text):
        return self.is_visible(username_text)

    def click_random_movie(self):
        random_movie_title = self.get_random_movie_title()
        self.click(random_movie_title)