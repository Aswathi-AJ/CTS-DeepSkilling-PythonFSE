"""
# Task 1: Organise Scripts into pytest Tests (Steps 40-44)
# Task 2: Parameterisation, Reporting and Screenshot on Failure (Steps 45-49)
"""

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# ------------------------------------------------------------------------------
# STEP 48: Session-Scoped Base URL Fixture
# ------------------------------------------------------------------------------
@pytest.fixture(scope="session")
def base_url():
    """
    Session-scoped fixture providing the base URL constant for all tests.
    Avoids hardcoding URLs across test modules.
    """
    return "https://www.lambdatest.com/selenium-playground/"


# ------------------------------------------------------------------------------
# STEP 41: Function-Scoped Driver Setup & Teardown Fixture
# ------------------------------------------------------------------------------
@pytest.fixture(scope="function")
def driver(request):
    """
    Function-scoped driver fixture.
    Creates a fresh headless Chrome browser instance for every test function,
    yields the driver, and handles browser cleanup in teardown.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,800")

    service = Service(ChromeDriverManager().install())
    driver_instance = webdriver.Chrome(service=service, options=options)
    driver_instance.implicitly_wait(5)

    # Attach driver instance to request node for failure screenshot hook access
    request.node.driver = driver_instance

    yield driver_instance

    # Teardown phase after yield
    driver_instance.quit()


# ------------------------------------------------------------------------------
# STEP 46: Pytest Hook for Screenshot Capture on Test Failure
# ------------------------------------------------------------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook executed for each test phase (setup, call, teardown).
    If a test execution phase fails, captures a browser screenshot automatically.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = getattr(item, "driver", None)
        if driver:
            test_name = item.name.replace("[", "_").replace("]", "_")
            screenshot_dir = os.path.join(os.path.dirname(__file__), "reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{test_name}_failure.png")
            driver.save_screenshot(screenshot_path)
            print(f"\n[Screenshot Hook] Test failed! Saved screenshot to: {screenshot_path}")
