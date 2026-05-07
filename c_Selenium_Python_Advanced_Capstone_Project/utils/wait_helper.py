from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# if element not visible within 10 seconds shows error 
def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )

# 10is maximum waiting time 
def wait_for_clickable(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def wait_for_dom(driver, timeout=10):
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )