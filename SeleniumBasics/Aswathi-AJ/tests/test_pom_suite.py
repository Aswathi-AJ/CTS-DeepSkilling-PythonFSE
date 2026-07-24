"""
# Task 2: Refactor Tests to Use POM and Build the Full Suite (Steps 55-59)

================================================================================
STEP 59: PAGE OBJECT MODEL MAINTENANCE BENEFIT EXPLANATION
================================================================================
PROBLEM IN FLAT (NON-POM) SCRIPTS:
- If the Submit button's ID changes from 'submit' to 'btn-submit' in the HTML UI,
  every single flat test script across the automation repository that contains hardcoded
  `driver.find_element(By.ID, 'submit')` calls will break simultaneously (e.g. 50+ failing tests).
- Maintaining flat scripts requires searching and updating dozens of individual test files,
  leading to tedious, error-prone, and unsustainable maintenance overhead.

HOW PAGE OBJECT MODEL (POM) SOLVES THIS:
- POM decouples test logic (assertions) from UI locator implementations.
- The Submit button locator is defined in exactly ONE place: `SimpleFormPage.SUBMIT_BUTTON = (By.ID, 'btn-submit')`.
- When the developer updates the element ID, only ONE line in ONE page file needs to be updated.
- All 50+ test scripts continue running without modifying a single line of test code!
================================================================================
"""

import pytest
from pages.simple_form_page import SimpleFormPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.input_form_page import InputFormPage


# ------------------------------------------------------------------------------
# STEP 55: Refactored Simple Form Submission Test Using SimpleFormPage
# ------------------------------------------------------------------------------
@pytest.mark.parametrize("message", ["Hello Selenium", "POM Testing", "12345"])
def test_simple_form_submission(driver, base_url, message):
    """
    Step 55: Test simple form submission using SimpleFormPage.
    Notice ZERO driver.find_element calls exist in this test function.
    """
    page = SimpleFormPage(driver)
    page.navigate()
    page.enter_message(message)
    page.click_submit()

    assert page.get_displayed_message() == message, f"Expected '{message}', but got '{page.get_displayed_message()}'"


# ------------------------------------------------------------------------------
# STEP 56: Refactored Checkbox Demo Test Using CheckboxPage
# ------------------------------------------------------------------------------
def test_checkbox_demo(driver, base_url):
    """
    Step 56: Test checkbox interactions using CheckboxPage object.
    """
    page = CheckboxPage(driver)
    page.navigate()

    # Test single checkbox
    assert not page.is_single_checkbox_checked(), "Checkbox should initially be unchecked."
    page.check_single_checkbox()
    assert page.is_single_checkbox_checked(), "Checkbox should be checked after click."

    # Test option checkbox
    page.check_option(0)
    assert page.is_option_checked(0), "Option 1 should be checked."
    page.uncheck_option(0)
    assert not page.is_option_checked(0), "Option 1 should be unchecked."


# ------------------------------------------------------------------------------
# STEP 56: Refactored Select Dropdown Test Using DropdownPage
# ------------------------------------------------------------------------------
def test_dropdown_selection(driver, base_url):
    """
    Step 56: Test select dropdown using DropdownPage object.
    """
    page = DropdownPage(driver)
    page.navigate()

    page.select_day("Wednesday")
    assert page.get_selected_day() == "Wednesday", f"Expected 'Wednesday', got '{page.get_selected_day()}'"


# ------------------------------------------------------------------------------
# STEP 57: Input Form Submit Test Using InputFormPage
# ------------------------------------------------------------------------------
def test_input_form_submit(driver, base_url):
    """
    Step 57: Test full input form submission using InputFormPage.
    Fills multiple input fields, submits form, and asserts success message.
    """
    page = InputFormPage(driver)
    page.navigate()

    page.fill_form(
        name="Aswathi AJ",
        email="aswathi@example.com",
        password="SecurePassword123",
        company="Cognizant",
        website="https://www.cognizant.com",
        country="United States",
        city="New York",
        address1="123 Tech Park Way",
        address2="Suite 400",
        state="NY",
        zipcode="10001"
    )
    page.submit_form()

    success_text = page.get_success_message()
    print(f"\n[Step 57] Input Form Submit Success Message: '{success_text}'")
    assert "Thanks for contacting us" in success_text or "successfully" in success_text.lower(), f"Unexpected success message: '{success_text}'"
