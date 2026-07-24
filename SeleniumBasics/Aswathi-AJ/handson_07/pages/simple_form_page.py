"""
# Task 1: Build Page Classes for the Selenium Playground (Steps 51-52)
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from handson_07.pages.base_page import BasePage


class SimpleFormPage(BasePage):
    """
    Step 51 & 52: SimpleFormPage encapsulating locators and actions for Simple Form Demo.
    All locators are defined as class-level tuples.
    Zero assertion statements inside page methods!
    """

    MESSAGE_INPUT = (By.ID, "user-message")
    SUBMIT_BUTTON = (By.ID, "showInput")
    DISPLAYED_MESSAGE = (By.ID, "message")

    def navigate(self):
        """Navigates to Simple Form Demo page."""
        self.navigate_to_path("simple-form-demo/")

    def enter_message(self, text: str):
        """Step 52: Enters message text into the input field."""
        elem = self.wait_for_element(self.MESSAGE_INPUT)
        elem.clear()
        elem.send_keys(text)

    def click_submit(self):
        """Step 52: Clicks the submit button."""
        btn = self.wait_for_element(self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].click();", btn)

    def get_displayed_message(self) -> str:
        """Step 52: Returns the displayed message text."""
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(
            lambda d: d.find_element(*self.DISPLAYED_MESSAGE) if d.find_element(*self.DISPLAYED_MESSAGE).text.strip() != "" else False
        )
        return elem.text
