from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # from your screenshot — data-testid="add-new-note"
    ADD_BTN = (By.CSS_SELECTOR, "[data-testid='add-new-note']")

    def is_logged_in(self):
        return "app" in self.driver.current_url

    def click_add(self):
        self.click(self.ADD_BTN)