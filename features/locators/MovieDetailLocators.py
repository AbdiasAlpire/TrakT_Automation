from selenium.webdriver.common.by import By

add_to_history_button = (By.CSS_SELECTOR, ".btn.btn-block.btn-summary.btn-watch.grid-item")
not_yet_add_to_history_button = (By.CSS_SELECTOR, ".btn.btn-block.btn-summary.btn-watch.grid-item.selected")
user_dropdown_section = (By.CSS_SELECTOR, ".btn.btn-profile.with-ul-menu.with-solid-bg")
history_user_dropdown_option = (By.XPATH, "//a[normalize-space()='History']")
current_movie_text = (By.CSS_SELECTOR, "body > div:nth-child(9) > section:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h1:nth-child(1)")
all_plays_button = (By.XPATH, "(//button[normalize-space()='All plays'])[1]")