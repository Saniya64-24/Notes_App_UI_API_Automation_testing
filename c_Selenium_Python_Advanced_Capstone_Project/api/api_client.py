import requests
from config.environment import get_config

config = get_config()

class APIClient:
    def __init__(self):
        self.base    = config["api_url"]
        self.token   = None
        self.headers = {}

    def login(self):
        r = requests.post(f"{self.base}/users/login", json={
            "email":    config["username"],
            "password": config["password"]
        })
        self.token   = r.json()["data"]["token"]
        self.headers = {"x-auth-token": self.token}

    def get_notes(self):
        return requests.get(f"{self.base}/notes", headers=self.headers)

    def create_note(self, title, desc):
        return requests.post(f"{self.base}/notes", headers=self.headers,
                             json={"title": title, "description": desc, "category": "Home"})

    def delete_note(self, note_id):
        return requests.delete(f"{self.base}/notes/{note_id}", headers=self.headers)