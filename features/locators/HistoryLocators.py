from selenium.webdriver.common.by import By

history_title = (By.CSS_SELECTOR, "h3[class='ellipsify']")
movie_title_on_history = (By.XPATH, "(//h3)[5]")
alert_of_no_history = (By.CSS_SELECTOR, ".alert.alert-no-data")
