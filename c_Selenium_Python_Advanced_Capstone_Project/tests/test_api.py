import allure
import pytest
import requests
from api.api_client import APIClient
from config.environment import get_config
from utils.logger import logger

config = get_config()

@allure.feature("API")
def test_get_notes():
    logger.info("Starting GET /notes API test")

    api = APIClient()
    api.login()

    logger.info("Fetching notes from API")
    r = api.get_notes()

    allure.attach(
        r.text,
        name="GET Notes Response",
        attachment_type=allure.attachment_type.JSON
    )

    logger.info(f"Status Code: {r.status_code}")

    assert r.status_code == 200
    assert isinstance(r.json()["data"], list)

    logger.info("GET /notes API test passed")

# -----------------------------
#           FR-08
# -----------------------------

#API response timeshould be less than 2 seconds
@allure.feature("API")
def test_api_response_time():
    api = APIClient()
    api.login()
    r = api.get_notes()
    assert r.elapsed.total_seconds() < 2


# -----------------------------
#           FR-06
# -----------------------------

#deleting the note via API
@allure.feature("API")
def test_delete_note():
    api = APIClient()
    api.login()
    r = api.create_note("Delete Me", "Will be deleted")
    note_id = r.json()["data"]["id"]
    r = api.delete_note(note_id)
    assert r.status_code == 200
    notes = api.get_notes().json()["data"]
    allure.attach(
        str(notes),
        name="API Notes Data",
        attachment_type=allure.attachment_type.JSON
    )
    assert not any(n["id"] == note_id for n in notes)


# -----------------------------
#           FR-09(API)
# -----------------------------

#Api negative test cases 
# getting note without token
@allure.feature("API - Negative")
def test_get_notes_no_token():
    r = requests.get(f"{config['api_url']}/notes")
    assert r.status_code == 401

# checking what happens when try to delete the non existing note or no note available
@allure.feature("API - Negative")
def test_delete_nonexistent_note():
    api = APIClient()
    api.login()
    r = api.delete_note("nonexistent-id-999")
    assert r.status_code == 400

# adding requirement to check creating note with missing fields
@allure.feature("API - Negative")
def test_create_note_missing_fields():
    api = APIClient()
    api.login()
    r = requests.post(
        f"{config['api_url']}/notes",
        headers=api.headers,
        json={}
    )
    assert r.status_code == 400