import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver(request):
    options = Options()
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("--start-maximized")

    # use chromedriver.exe from project folder if exists
    # otherwise use ChromeDriverManager
    chromedriver_path = "chromedriver.exe"
    if os.path.exists(chromedriver_path):
        service = Service(chromedriver_path)
    else:
        from webdriver_manager.chrome import ChromeDriverManager
        driver_path = ChromeDriverManager().install()
        if not driver_path.endswith(".exe"):
            driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe")
        service = Service(driver_path)

    drv = webdriver.Chrome(service=service, options=options)
    drv.maximize_window()
    yield drv

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        drv.save_screenshot(f"screenshots/{request.node.name}.png")
        print(f"\nScreenshot saved: screenshots/{request.node.name}.png")

    drv.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)