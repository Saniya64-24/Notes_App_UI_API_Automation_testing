import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# ---------- Screenshot Function ----------
def take_screenshot(driver, test_name):

    os.makedirs("screenshots", exist_ok=True)

    path = f"screenshots/{test_name}.png"

    driver.save_screenshot(path)

    print(f"\nScreenshot saved: {path}")


# ---------- Pytest Hook ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


# ---------- Driver Fixture ----------
@pytest.fixture
def driver(request):

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)

    # driver.maximize_window()

    yield driver


    # ---------- Screenshot on failure ----------
    if request.node.rep_call.failed:

        test_name = request.node.name

        try:
            take_screenshot(driver, test_name)
        except:
            print("Could not take screenshot")

    driver.quit()