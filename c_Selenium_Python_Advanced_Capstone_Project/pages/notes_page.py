from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class NotesPage(BasePage):
    CATEGORY = (By.CSS_SELECTOR, "[data-testid='note-category']")
    TITLE    = (By.CSS_SELECTOR, "[data-testid='note-title']")
    DESC     = (By.CSS_SELECTOR, "[data-testid='note-description']")
    SAVE     = (By.CSS_SELECTOR, "[data-testid='note-submit']")
    TITLES   = (By.CSS_SELECTOR, "[data-testid='note-card-title']")

    def create_note(self, title, desc, category="Home"):
        el = self.wait.until(EC.presence_of_element_located(self.CATEGORY))
        Select(el).select_by_visible_text(category)
        self.type(self.TITLE, title)
        self.type(self.DESC, desc)
        self.click(self.SAVE)
        time.sleep(2)   # wait for modal to close and note to appear

    def get_titles(self):
        return [e.text for e in self.driver.find_elements(*self.TITLES)]

    def note_exists(self, title):
        return title in self.get_titles()