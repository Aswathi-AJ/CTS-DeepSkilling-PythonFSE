"""
# Task 1: Organise Scripts into pytest Tests (Steps 40-44)
# Task 2: Parameterisation, Reporting and Screenshot on Failure (Steps 45-49)
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("message", ["Hello", "Selenium Automation", "12345"])
def test_simple_form_submission(driver, base_url, message):
    """
    Step 40 & 42 & 45: Opens Simple Form Demo, enters message input,
    clicks Get Checked Value, and asserts displayed message equals input parameter.
    """
    driver.get(base_url)
    driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

    wait = WebDriverWait(driver, 10)
    user_input = wait.until(EC.presence_of_element_located((By.ID, "user-message")))
    user_input.clear()
    user_input.send_keys(message)

    show_btn = wait.until(EC.presence_of_element_located((By.ID, "showInput")))
    driver.execute_script("arguments[0].click();", show_btn)

    displayed_elem = wait.until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert displayed_elem.text == message, f"Expected '{message}', but got '{displayed_elem.text}'"


def test_checkbox_demo(driver, base_url):
    """
    Step 43: Opens Checkbox Demo via landing page link, clicks single checkbox, asserts is_selected() is True,
    clicks again, asserts is_selected() is False.
    """
    driver.get(base_url)
    driver.find_element(By.LINK_TEXT, "Checkbox Demo").click()

    wait = WebDriverWait(driver, 10)
    checkbox = wait.until(EC.presence_of_element_located((By.ID, "isAgeSelected")))

    assert not checkbox.is_selected(), "Checkbox was initially selected!"
    driver.execute_script("arguments[0].click();", checkbox)
    assert checkbox.is_selected(), "Checkbox was not selected after click!"
    driver.execute_script("arguments[0].click();", checkbox)
    assert not checkbox.is_selected(), "Checkbox was still selected after second click!"


def test_dropdown_selection(driver, base_url):
    """
    Step 49: Opens Select Dropdown List demo via landing page link, uses Select class to choose 'Wednesday',
    and asserts selected option text is 'Wednesday'.
    """
    driver.get(base_url)
    driver.find_element(By.LINK_TEXT, "Select Dropdown List").click()

    wait = WebDriverWait(driver, 10)
    dropdown_elem = wait.until(EC.presence_of_element_located((By.ID, "select-demo")))
    select = Select(dropdown_elem)

    select.select_by_visible_text("Wednesday")

    selected_option = select.first_selected_option.text
    assert selected_option == "Wednesday", f"Expected 'Wednesday', but got '{selected_option}'"
