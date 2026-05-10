from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.self_healing import find_element_with_healing


def test_login():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.get("https://practice.expandtesting.com/login")

    element = find_element_with_healing(
        driver,
        "//button[@id='wrong-login-btn']"
    )

    print("Element found")

    driver.quit()


