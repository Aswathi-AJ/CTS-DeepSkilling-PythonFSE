"""
# Task 1: Build Page Classes for the Selenium Playground (Step 54)
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):
    """
    Step 54: DropdownPage encapsulating locators and actions for Select Dropdown page.
    Uses Selenium Select class internally.
    """

    DAY_DROPDOWN = (By.ID, "select-demo")

    def navigate(self):
        """Navigates to Select Dropdown page."""
        self.navigate_to_path("select-dropdown-demo/")

    def select_day(self, day_name: str):
        """Step 54: Selects a day by visible text using Select class."""
        elem = self.wait_for_element(self.DAY_DROPDOWN)
        select = Select(elem)
        select.select_by_visible_text(day_name)

    def get_selected_day(self) -> str:
        """Returns the currently selected day text."""
        elem = self.wait_for_element(self.DAY_DROPDOWN)
        select = Select(elem)
        return select.first_selected_option.text
