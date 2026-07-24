"""
# Task 1: Build Page Classes for the Selenium Playground (Step 50)
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Step 50: BasePage class encapsulating common driver actions, navigation,
    and explicit wait utilities shared by all page object classes.
    """

    BASE_URL = "https://www.lambdatest.com/selenium-playground/"

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url: str):
        """Navigates to the specified full URL."""
        self.driver.get(url)

    def navigate_to_path(self, relative_path: str):
        """Navigates to relative endpoint under base URL."""
        url = self.BASE_URL.rstrip('/') + '/' + relative_path.lstrip('/')
        self.driver.get(url)

    def get_title(self) -> str:
        """Returns the current page title."""
        return self.driver.title

    def wait_for_element(self, locator: tuple, timeout: int = 10):
        """Waits for an element specified by locator tuple to become visible in DOM."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_clickable(self, locator: tuple, timeout: int = 10):
        """Waits for an element specified by locator tuple to become clickable."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
