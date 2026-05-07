import allure
import requests
from api.api_client import APIClient
from config.environment import get_config

config = get_config()

@allure.feature("API")
def test_get_notes():                                  # TC-006
    api = APIClient()
    api.login()
    r = api.get_notes()
    assert r.status_code == 200
    assert isinstance(r.json()["data"], list)

@allure.feature("API")
def test_api_response_time():                          # TC-007
    api = APIClient()
    api.login()
    r = api.get_notes()
    assert r.elapsed.total_seconds() < 2

@allure.feature("API")
def test_delete_note():                                # TC-009
    api = APIClient()
    api.login()
    # create a note first
    r = api.create_note("Delete Me", "Will be deleted")
    note_id = r.json()["data"]["id"]
    # delete it
    r = api.delete_note(note_id)
    assert r.status_code == 200
    # confirm gone from API
    notes = api.get_notes().json()["data"]
    assert not any(n["id"] == note_id for n in notes)

@allure.feature("API - Negative")
def test_get_notes_no_token():                         # TC-012
    r = requests.get(f"{config['api_url']}/notes")
    assert r.status_code == 401

@allure.feature("API - Negative")
def test_delete_nonexistent_note():                    # TC-013
    api = APIClient()
    api.login()
    r = api.delete_note("nonexistent-id-999")
    assert r.status_code == 400

@allure.feature("API - Negative")
def test_create_note_missing_fields():                 # TC-014
    api = APIClient()
    api.login()
    r = requests.post(
        f"{config['api_url']}/notes",
        headers=api.headers,
        json={}
    )
    assert r.status_code == 400