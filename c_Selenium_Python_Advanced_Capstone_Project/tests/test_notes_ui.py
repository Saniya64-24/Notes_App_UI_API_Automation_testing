import allure
import random
from c_Selenium_Python_Advanced_Capstone_Project.utils.logger import logger
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.notes_page import NotesPage
from config.environment import get_config
from api.api_client import APIClient

config = get_config()

def do_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login(config["username"], config["password"])
    return HomePage(driver)

# -----------------------------
#           FR-02              
# -----------------------------
#creating notes via UI
@allure.feature("Notes UI")
def test_create_note(driver):
    home = do_login(driver)

    random_value=random.randint(1000,9999)

    home.click_add()
    notes = NotesPage(driver)

    notes.create_note(f"My Test Note {random_value}", f"This is a test description {random_value}")
    assert notes.note_exists(f"My Test Note {random_value}")


# -----------------------------
#           FR-03
# -----------------------------
# test note appears quickly  after crating 
@allure.feature("Notes UI")
def test_note_appears_instantly_without_refresh(driver):   # FR-03
    home = do_login(driver)
    home.click_add()

    notes = NotesPage(driver)
    notes.create_note("Instant Visible Note", "FR-03 check")

    # do NOT refresh — note must appear immediately in DOM
    titles = notes.get_titles()
    assert "Instant Visible Note" in titles, \
        "FR-03 FAILED — note did not appear instantly without page refresh"


# -----------------------------
#           FR-04
# -----------------------------

# getting list output 
@allure.feature("API")
def test_get_notes_returns_list():
    api = APIClient()
    api.login()
    r = api.get_notes()
    assert r.status_code == 200
    assert isinstance(r.json()["data"], list)

# adding check not FR asked for 
#UI response timeshould be less than 2 seconds 
@allure.feature("Performance")
def test_ui_load_time(driver):
    page = LoginPage(driver)
    page.open()
    page.wait_for_dom()
    timing = page.get_ui_timing()
    print(f"\nUI Load Time: {timing}ms")
    assert timing < 2000    #page  must load within  2 soconds
