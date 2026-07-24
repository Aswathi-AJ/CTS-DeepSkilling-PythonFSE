"""
# Task 1: Build Page Classes for the Selenium Playground (Step 53)
"""

from selenium.webdriver.common.by import By
from handson_07.pages.base_page import BasePage


class CheckboxPage(BasePage):
    """
    Step 53: CheckboxPage encapsulating locators and interactions for Checkbox Demo.
    """

    SINGLE_CHECKBOX = (By.ID, "isAgeSelected")
    OPTION_CHECKBOXES = (By.CSS_SELECTOR, "input.cb1-element")

    def navigate(self):
        """Navigates to Checkbox Demo page."""
        self.navigate_to_path("checkbox-demo/")

    def check_single_checkbox(self):
        """Checks the single checkbox if not already checked."""
        elem = self.wait_for_element(self.SINGLE_CHECKBOX)
        if not elem.is_selected():
            self.driver.execute_script("arguments[0].click();", elem)

    def uncheck_single_checkbox(self):
        """Unchecks the single checkbox if checked."""
        elem = self.wait_for_element(self.SINGLE_CHECKBOX)
        if elem.is_selected():
            self.driver.execute_script("arguments[0].click();", elem)

    def is_single_checkbox_checked(self) -> bool:
        """Returns boolean state of the single checkbox."""
        elem = self.wait_for_element(self.SINGLE_CHECKBOX)
        return elem.is_selected()

    def check_option(self, index: int):
        """Step 53: Checks option checkbox by 0-based index."""
        elements = self.driver.find_elements(*self.OPTION_CHECKBOXES)
        if 0 <= index < len(elements):
            if not elements[index].is_selected():
                self.driver.execute_script("arguments[0].click();", elements[index])

    def uncheck_option(self, index: int):
        """Step 53: Unchecks option checkbox by 0-based index."""
        elements = self.driver.find_elements(*self.OPTION_CHECKBOXES)
        if 0 <= index < len(elements):
            if elements[index].is_selected():
                self.driver.execute_script("arguments[0].click();", elements[index])

    def is_option_checked(self, index: int) -> bool:
        """Step 53: Returns check state of option checkbox by 0-based index."""
        elements = self.driver.find_elements(*self.OPTION_CHECKBOXES)
        if 0 <= index < len(elements):
            return elements[index].is_selected()
        return False
