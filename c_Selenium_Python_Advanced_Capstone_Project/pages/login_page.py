from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL        = (By.ID, "email")
    PASSWORD     = (By.ID, "password")
    BTN          = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR        = (By.CSS_SELECTOR, "[data-testid='alert-message']")
    FIELD_ERROR  = (By.CSS_SELECTOR, ".invalid-feedback")

    def open(self):
        self.driver.get("https://practice.expandtesting.com/notes/app/login")

    def login(self, email, password):
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.BTN)


















# from selenium.webdriver.common.by import By
# from pages.base_page import BasePage

# class LoginPage(BasePage):
#     EMAIL    = (By.ID, "email")
#     PASSWORD = (By.ID, "password")
#     BTN      = (By.CSS_SELECTOR, "button[type='submit']")
#     ERROR    = (By.CSS_SELECTOR, "[data-testid='alert-message']")
#     INVALID_EMAIL_ERROR = (By.ID, "email")

#     def open(self):
#         self.driver.get("https://practice.expandtesting.com/notes/app/login")

#     def login(self, email, password):
#         self.type(self.EMAIL, email)
#         self.type(self.PASSWORD, password)
#         self.click(self.BTN)
    
#     def get_error(self):
#         return self.get_text(self.ERROR)
    
#     def get_invalid_email_error(self):
#         element = self.wait.until(
#             lambda d: d.find_element(*self.INVALID_EMAIL_ERROR)
#         )

#         return element.get_attribute("validationMessage")