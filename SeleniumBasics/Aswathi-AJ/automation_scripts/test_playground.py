"""
# Task 1: Organise Scripts into pytest Tests (Steps 40-44)
# Task 2: Parameterisation, Reporting and Screenshot on Failure (Steps 45-49)
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


# ------------------------------------------------------------------------------
# STEP 40 & 42 & 45: Parameterised Simple Form Submission Test
# ------------------------------------------------------------------------------
@pytest.mark.parametrize("message", ["Hello", "Selenium Automation", "12345"])
def test_simple_form_submission(driver, base_url, message):
    """
    Step 40 & 42 & 45: Opens Simple Form Demo, enters message input,
    clicks Get Checked Value, and asserts displayed message equals input parameter.
    Runs 3 times with different test data sets.
    """
    driver.get(base_url + "simple-form-demo")

    # Locate user message input field
    user_input = driver.find_element(By.ID, "user-message")
    user_input.clear()
    user_input.send_keys(message)

    # Click 'Get Checked Value' button
    show_btn = driver.find_element(By.ID, "showInput")
    show_btn.click()

    # Wait for displayed message element
    wait = WebDriverWait(driver, 5)
    displayed_elem = wait.until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    # Assertion
    assert displayed_elem.text == message, f"Expected '{message}', but got '{displayed_elem.text}'"


# ------------------------------------------------------------------------------
# STEP 43: Checkbox Interaction Test
# ------------------------------------------------------------------------------
def test_checkbox_demo(driver, base_url):
    """
    Step 43: Opens Checkbox Demo, clicks single checkbox, asserts is_selected() is True,
    clicks again, asserts is_selected() is False.
    """
    driver.get(base_url + "checkbox-demo")

    checkbox = driver.find_element(By.ID, "isAgeSelected")

    # Initial state should be unchecked
    assert not checkbox.is_selected(), "Checkbox was initially selected!"

    # Click to check
    checkbox.click()
    assert checkbox.is_selected(), "Checkbox was not selected after click!"

    # Click to uncheck
    checkbox.click()
    assert not checkbox.is_selected(), "Checkbox was still selected after second click!"


# ------------------------------------------------------------------------------
# STEP 49: Select Dropdown List Test using Select Class
# ------------------------------------------------------------------------------
def test_dropdown_selection(driver, base_url):
    """
    Step 49: Opens Select Dropdown List demo, uses Selenium Select class to choose 'Wednesday',
    and asserts selected option text is 'Wednesday'.
    """
    driver.get(base_url + "select-dropdown-demo")

    dropdown_elem = driver.find_element(By.ID, "select-demo")
    select = Select(dropdown_elem)

    # Select by visible text
    select.select_by_visible_text("Wednesday")

    selected_option = select.first_selected_option.text
    assert selected_option == "Wednesday", f"Expected 'Wednesday', but got '{selected_option}'"
