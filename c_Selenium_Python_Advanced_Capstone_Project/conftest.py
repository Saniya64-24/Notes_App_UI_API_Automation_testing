import allure
import pytest
import os
# from config import grid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture
def driver(request):
    options = Options()
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("--start-maximized")

    GRID = True

    if GRID:
        drv = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options
        )
    else:
        service = Service(ChromeDriverManager().install())
        drv = webdriver.Chrome(service=service, options=options)

        drv = webdriver.Chrome(service=service, options=options)

    yield drv

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)

        screenshot_path = f"screenshots/{request.node.name}.png"

        drv.save_screenshot(screenshot_path)

        allure.attach.file(
            screenshot_path,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

        print(f"\nScreenshot saved: {screenshot_path}")
        
    drv.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)















# import pytest
# import os

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


# # ---------- Screenshot Function ----------
# def take_screenshot(driver, test_name):

#     os.makedirs("screenshots", exist_ok=True)

#     path = f"screenshots/{test_name}.png"

#     driver.save_screenshot(path)

#     print(f"\nScreenshot saved: {path}")


# # ---------- Pytest Hook ----------
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):

#     outcome = yield

#     rep = outcome.get_result()

#     setattr(item, "rep_" + rep.when, rep)


# # ---------- Driver Fixture ----------
# @pytest.fixture
# def driver(request):

#     service = Service(ChromeDriverManager().install())

#     driver = webdriver.Chrome(service=service)

#     # driver.maximize_window()

#     yield driver


#     # ---------- Screenshot on failure ----------
#     if request.node.rep_call.failed:

#         test_name = request.node.name

#         try:
#             take_screenshot(driver, test_name)
#         except:
#             print("Could not take screenshot")

#     driver.quit()