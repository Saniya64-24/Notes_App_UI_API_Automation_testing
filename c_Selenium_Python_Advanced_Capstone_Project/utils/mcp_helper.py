import requests
import json
from utils.logger import logger
from config.environment import get_config

config = get_config()

def generate_test_note():
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": config["anthropic_api_key"],
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 100,
                "messages": [{
                    "role": "user",
                    "content": 'Generate a realistic note title and description for a notes app. Reply only in JSON with no extra text: {"title": "...", "description": "..."}'
                }]
            }
        )
        text = response.json()["content"][0]["text"]
        note = json.loads(text)
        logger.info(f"MCP generated — Title: {note['title']}")
        return note["title"], note["description"]

    except Exception as e:
        # fallback if API fails
        logger.info(f"MCP fallback used — {str(e)}")
        return "Fallback Note 1234", "Fallback description 1234"


def analyze_failure(test_name, error_msg):
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": config["anthropic_api_key"],
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 100,
                "messages": [{
                    "role": "user",
                    "content": f"Selenium test '{test_name}' failed with: {error_msg[:300]}. In one sentence what is the likely cause and fix?"
                }]
            }
        )
        suggestion = response.json()["content"][0]["text"]
        logger.info(f"MCP suggestion for {test_name}: {suggestion}")
        return suggestion

    except Exception as e:
        return "Check screenshot and logs for details."