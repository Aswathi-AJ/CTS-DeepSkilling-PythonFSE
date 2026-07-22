"""
# Task 1: Selenium Architecture and Environment Setup (Steps 24-27)
# Task 2: WebDriver Navigation and Window Commands (Steps 28-31)

================================================================================
STEP 24: SELENIUM ARCHITECTURE OVERVIEW
================================================================================
1. SELENIUM WEBDRIVER:
   - What it is: A web framework that permits executing cross-browser automated tests.
   - Communication Mechanism: Communicates directly with the browser using native browser automation APIs
     via W3C WebDriver Protocol over HTTP RESTful endpoints.

2. SELENIUM GRID:
   - Problem Solved: Solves the bottleneck of sequential single-machine test execution.
   - Capabilities: Enables scaling and running tests in parallel across diverse distributed nodes,
     operating systems (Windows, Linux, macOS), and browser types/versions simultaneously.

3. SELENIUM IDE:
   - What it is: A lightweight Chrome/Firefox browser extension for fast prototyping.
   - Purpose: Used for quick record-and-playback of user browser interactions, script debugging,
     and exporting basic test code into language bindings like Python, Java, or C#.
================================================================================
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def run_setup_and_navigation_demo():
    print("=== Running Hands-On 4: Selenium WebDriver Setup & Commands ===")

    # --------------------------------------------------------------------------
    # STEP 27: ChromeOptions & Headless Mode Setup
    # --------------------------------------------------------------------------
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # STEP 25: WebDriver Initialization using webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # ----------------------------------------------------------------------
        # STEP 26: Implicit Wait Demonstration & Bad Practice Note
        # ----------------------------------------------------------------------
        driver.implicitly_wait(10)
        """
        WHY GLOBAL IMPLICIT WAIT IS BAD PRACTICE:
        1. Implicit waits apply globally to all element searches (driver.find_element).
        2. Mixing implicit and explicit waits causes unpredictable wait times.
        3. Implicit wait only polls for element existence in DOM, NOT whether it is visible, clickable, or enabled.
        4. Explicit waits (WebDriverWait) provide precise, element-specific conditions and avoid hidden slowdowns.
        """

        # STEP 25: Navigate to LambdaTest Selenium Playground and print page title
        base_url = "https://www.lambdatest.com/selenium-playground/"
        driver.get(base_url)
        print(f"[Step 25] Page Title: '{driver.title}'")
        assert "Selenium Grid Online" in driver.title or "LambdaTest" in driver.title

        # ----------------------------------------------------------------------
        # STEP 28: Navigation Commands & Current URL Assertion
        # ----------------------------------------------------------------------
        simple_form_link = driver.find_element(By.LINK_TEXT, "Simple Form Demo")
        simple_form_link.click()

        current_url = driver.current_url
        print(f"[Step 28] Current URL after click: {current_url}")
        assert "simple-form-demo" in current_url, "URL does not contain 'simple-form-demo'"

        driver.back()
        print(f"[Step 28] URL after driver.back(): {driver.current_url}")

        # ----------------------------------------------------------------------
        # STEP 29: Window Handles, Switch to New Tab & Tab Title
        # ----------------------------------------------------------------------
        driver.execute_script('window.open("https://www.google.com");')
        all_handles = driver.window_handles
        print(f"[Step 29] Open Window Handles Count: {len(all_handles)}")

        # Switch to newly opened tab (index 1)
        driver.switch_to.window(all_handles[1])
        google_title = driver.title
        print(f"[Step 29] Title of New Tab: '{google_title}'")

        # ----------------------------------------------------------------------
        # STEP 30: Switch Back to Original Tab & Capture Screenshot
        # ----------------------------------------------------------------------
        driver.switch_to.window(all_handles[0])
        screenshot_filename = "playground_screenshot.png"
        driver.save_screenshot(screenshot_filename)
        assert os.path.exists(screenshot_filename), "Screenshot file was not saved!"
        print(f"[Step 30] Screenshot saved successfully: {os.path.abspath(screenshot_filename)}")

        # ----------------------------------------------------------------------
        # STEP 31: Window Sizing Commands & Explanation
        # ----------------------------------------------------------------------
        original_size = driver.get_window_size()
        print(f"[Step 31] Original Window Size: Width={original_size['width']}, Height={original_size['height']}")

        driver.set_window_size(1280, 800)
        new_size = driver.get_window_size()
        print(f"[Step 31] Set Window Size: Width={new_size['width']}, Height={new_size['height']}")

        """
        WHY CONSISTENT WINDOW SIZE MATTERS IN UI AUTOMATION:
        1. Modern web apps use responsive CSS layouts (@media queries). Elements move, hide, or collapse into burger menus on small screens.
        2. Standardizing window dimensions (e.g. 1280x800) ensures consistent DOM element visibility, layout structure, and clickability across local dev and CI machines.
        """

    finally:
        driver.quit()
        print("[Step 25] Browser closed successfully.")


if __name__ == "__main__":
    run_setup_and_navigation_demo()
