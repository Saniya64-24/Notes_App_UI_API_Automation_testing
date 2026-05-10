from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def find_element_with_healing(driver, locator):

    try:
        print("Trying original locator")

        return driver.find_element(By.XPATH, locator)

    except NoSuchElementException:

        print("Original locator failed")

        # fake healed locator
        new_locator = "//button[contains(text(),'Login')]"

        print(f"Trying new locator: {new_locator}")

        return driver.find_element(By.XPATH, new_locator)