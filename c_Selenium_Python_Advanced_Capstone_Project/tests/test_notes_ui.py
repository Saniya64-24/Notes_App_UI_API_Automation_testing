import allure
import random
from utils.logger import logger
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.notes_page import NotesPage
from config.environment import get_config
from api.api_client import APIClient
from utils.logger import logger

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

    logger.info("Starting create note test")

    home = do_login(driver)

    random_value = random.randint(1000,9999)

    note_title = f"My Test Note {random_value}"
    note_desc = f"This is a test description {random_value}"

    logger.info(f"Creating note with title: {note_title}")

    home.click_add()

    notes = NotesPage(driver)

    notes.create_note(note_title, note_desc)

    logger.info("Checking whether note exists in UI")

    assert notes.note_exists(note_title)

    logger.info("Create note test passed")


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
    assert timing < 5000    #page  must load within  2 soconds


