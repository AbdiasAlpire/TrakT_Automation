from selenium.webdriver.common.by import By

email_input_locator = (By.ID, "user_login")
password_input_locator = (By.ID, "user_password")
login_button_locator = (By.CSS_SELECTOR, "input[value='Sign in']")
exit_link_locator = (By.CSS_SELECTOR, ".exit")