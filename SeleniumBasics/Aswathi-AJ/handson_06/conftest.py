"""
# Task 1: Organise Scripts into pytest Tests (Steps 40-44)
# Task 2: Parameterisation, Reporting and Screenshot on Failure (Steps 45-49)
"""

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def base_url():
    """Session-scoped base URL fixture."""
    return "https://www.lambdatest.com/selenium-playground/"


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
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver_instance = webdriver.Chrome(service=service, options=options)
    driver_instance.implicitly_wait(5)

    request.node.driver = driver_instance

    yield driver_instance

    driver_instance.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Failure screenshot hook."""
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
