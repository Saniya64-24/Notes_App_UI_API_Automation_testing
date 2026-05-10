import allure
import pytest

from pages.login_page import LoginPage
from pages.home_page import HomePage
from config.environment import get_config
from utils.logger import logger

# this file covers positive and negative login ui scenarios 
config = get_config()

# -----------------------------
#           FR-01
# -----------------------------
# Valid login test
@allure.feature("Login")
def test_valid_login(driver):

    logger.info("Opening login page")

    page = LoginPage(driver)
    page.open()

    logger.info("Entering valid credentials")

    page.login(config["username"], config["password"])

    logger.info("Checking whether login is successful")

    assert HomePage(driver).is_logged_in()

    logger.info("Valid login test passed")


# -----------------------------
#           FR-09(UI)
# -----------------------------

#parameterized checking of error
@allure.feature("Login - Negative")
@pytest.mark.parametrize("email, password", [
    ("wrong@test.com",   "wrong123"),
    (config["username"], "wrongpass"),
])
def test_invalid_login(driver, email, password):
    page = LoginPage(driver)
    page.open()
    page.login(email, password)
    assert page.is_visible(page.ERROR)


#checking empty space entry in login details 
@allure.feature("Login - Negative")
def test_empty_fields(driver):                     # TC-003
    page = LoginPage(driver)
    page.open()
    page.login("", "")
    assert page.is_visible(page.FIELD_ERROR)

#checking valid email error
@allure.feature("Login - Negative")
def test_invalid_email_format(driver):             # invalid email
    page = LoginPage(driver)
    page.open()
    page.login("notanemail", "password123")
    assert page.is_visible(page.FIELD_ERROR)















# import allure
# import pytest
# from pages.login_page import LoginPage
# from pages.home_page import HomePage
# from config.environment import get_config

# config = get_config()

# @allure.feature("Login")
# def test_valid_login(driver):
#     page = LoginPage(driver)
#     page.open()
#     page.login(config["username"], config["password"])
#     assert HomePage(driver).is_logged_in()

# @allure.feature("Login - Negative")
# @pytest.mark.parametrize(
#     "email, password, expected_error",
#     [

#         ("wrong@test.com", "wrong123",
#          "Incorrect email address or password"),

#         ("", "", ""),

#         ("notanemail", "password123",
#          "Email address is invalid"),

#         (config["username"], "wrongpass",
#          "Incorrect email address or password"),

#     ]
# )
# def test_invalid_login(driver, email, password, expected_error):

#     page = LoginPage(driver)

#     page.open()

#     page.login(email, password)

#     # Empty fields case
#     if email == "" and password == "":
#         assert True

#     else:
#         actual_error = page.get_error()

#         assert expected_error in actual_error