from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from utils.self_healing import find_element_with_healing

import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator, retries=3):
        for i in range(retries):
            try:
                el = self.wait.until(EC.element_to_be_clickable(locator))
                self.driver.execute_script("arguments[0].click();", el)  # JS executor
                return
            except StaleElementReferenceException:
                time.sleep(1)

    def type(self, locator, text):
        el = self.wait.until(EC.presence_of_element_located(locator))
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def wait_for_dom(self):
        # JS executor wait for page load
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def get_ui_timing(self):
        # UI performance timing via JS
        return self.driver.execute_script(
            "return window.performance.timing.loadEventEnd - window.performance.timing.navigationStart"
        )
    
    def find_with_fallback(self, primary, fallback):
        # self-healing — tries primary locator first then fallback
        try:
            return self.wait.until(EC.presence_of_element_located(primary))
        except:
            print(f"Primary locator failed, trying fallback")
            return self.wait.until(EC.presence_of_element_located(fallback))
    

    def click_login(driver):
        button = find_element_with_healing(
            driver,
            "//button[@id='login-btn']"
        )

        button.click()