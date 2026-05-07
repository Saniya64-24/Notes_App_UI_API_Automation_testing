import allure
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.notes_page import NotesPage
from api.api_client import APIClient
from config.environment import get_config

config = get_config()

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