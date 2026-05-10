import allure
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.notes_page import NotesPage
from api.api_client import APIClient
from config.environment import get_config
from c_Selenium_Python_Advanced_Capstone_Project.utils.logger import logger

config = get_config()

# -----------------------------
#           FR-05
# -----------------------------
#creating note in ui and fetching data from api used to check note creation and visibility
@allure.feature("E2E")
def test_ui_note_appears_in_api(driver):
    # Step 1 — create note via UI
    page = LoginPage(driver)
    page.open()
    page.login(config["username"], config["password"])
    HomePage(driver).click_add()
    NotesPage(driver).create_note("E2E Note", "Check in API")

    # Step 2 — fetch from API
    api = APIClient()
    api.login()
    notes = api.get_notes().json()["data"]

    # Step 3 — verify match
    titles = [n["title"] for n in notes]
    assert "E2E Note" in titles

# -----------------------------
#           FR-08
# -----------------------------
# delete note at api and see in ui to know wheather the note deleted or not
@allure.feature("E2E")
def test_api_delete_reflects_on_ui(driver):
    # Step 1 — create note via API
    api = APIClient()
    api.login()
    note_id = api.create_note("UI Delete Test", "delete me").json()["data"]["id"]

    # Step 2 — delete via API
    api.delete_note(note_id)

    # Step 3 — check UI
    page = LoginPage(driver)
    page.open()
    page.login(config["username"], config["password"])
    driver.refresh()

    notes = NotesPage(driver)
    assert not notes.note_exists("UI Delete Test")