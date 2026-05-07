import allure
import pytest
import requests
from api.api_client import APIClient
from config.environment import get_config

config = get_config()

@allure.feature("API")
def test_get_notes():
    api = APIClient()
    api.login()
    r = api.get_notes()
    assert r.status_code == 200
    assert isinstance(r.json()["data"], list)

@allure.feature("API")
def test_api_response_time():
    api = APIClient()
    api.login()
    r = api.get_notes()
    assert r.elapsed.total_seconds() < 2

@allure.feature("API")
def test_delete_note():
    api = APIClient()
    api.login()
    r = api.create_note("Delete Me", "Will be deleted")
    note_id = r.json()["data"]["id"]
    r = api.delete_note(note_id)
    assert r.status_code == 200
    notes = api.get_notes().json()["data"]
    assert not any(n["id"] == note_id for n in notes)

@allure.feature("API - Negative")
def test_get_notes_no_token():
    r = requests.get(f"{config['api_url']}/notes")
    assert r.status_code == 401

@allure.feature("API - Negative")
def test_delete_nonexistent_note():
    api = APIClient()
    api.login()
    r = api.delete_note("nonexistent-id-999")
    assert r.status_code == 400

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