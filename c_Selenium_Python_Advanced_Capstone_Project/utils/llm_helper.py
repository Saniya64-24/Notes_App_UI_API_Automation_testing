import requests

API_KEY = "ak_2Gx2Uv8uw28Y1dK6KQ62P7Tq0hg36"


def get_fixed_locator(failed_locator, html):
    prompt = f"""
    The following selenium locator failed:
    {failed_locator}

    Here is the page HTML:
    {html[:4000]}

    Suggest a better xpath locator only.
    """

    response = requests.post(
        "YOUR_LLM_ENDPOINT",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": "longcat",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    data = response.json()

    return data["choices"][0]["message"]["content"]