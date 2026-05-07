import allure
from c_Selenium_Python_Advanced_Capstone_Project.utils.logger import logger
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.notes_page import NotesPage
from config.environment import get_config

config = get_config()

def do_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login(config["username"], config["password"])
    return HomePage(driver)

@allure.feature("Notes UI")
def test_create_note(driver):
    home = do_login(driver)
    home.click_add()

    notes = NotesPage(driver)
    notes.create_note("My Test Note", "This is a test description")

    assert notes.note_exists("My Test Note")

@allure.feature("Notes UI - Negative")
def test_wrong_credentials(driver):                    # TC-011
    page = LoginPage(driver)
    page.open()
    page.login("wrong@email.com", "wrongpass")
    assert page.is_visible(page.ERROR)

@allure.feature("Performance")
def test_ui_load_time(driver):
    page = LoginPage(driver)
    page.open()
    page.wait_for_dom()
    timing = page.get_ui_timing()
    print(f"\nUI Load Time: {timing}ms")
    assert timing < 5000    # page  must load under 5 soconds