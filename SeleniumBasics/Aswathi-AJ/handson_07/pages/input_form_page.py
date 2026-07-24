"""
# Task 1: Build Page Classes for the Selenium Playground (Step 57)
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from handson_07.pages.base_page import BasePage


class InputFormPage(BasePage):
    """
    Step 57: InputFormPage encapsulating locators and actions for the Input Form Submit page.
    """

    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='Email']")
    PASSWORD_INPUT = (By.ID, "inputPassword4")
    COMPANY_INPUT = (By.ID, "company")
    WEBSITE_INPUT = (By.ID, "websitename")
    COUNTRY_DROPDOWN = (By.NAME, "country")
    CITY_INPUT = (By.ID, "inputCity")
    ADDRESS1_INPUT = (By.ID, "inputAddress1")
    ADDRESS2_INPUT = (By.ID, "inputAddress2")
    STATE_INPUT = (By.ID, "inputState")
    ZIP_INPUT = (By.ID, "inputZip")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MSG = (By.CSS_SELECTOR, "p.success-msg")

    def navigate(self):
        """Navigates to Input Form Submit page."""
        self.navigate_to_path("input-form-demo/")

    def fill_form(self, name, email, password, company, website, country, city, address1, address2, state, zipcode):
        """Step 57: Fills out all input form fields."""
        self.wait_for_element(self.NAME_INPUT).send_keys(name)
        self.wait_for_element(self.EMAIL_INPUT).send_keys(email)
        self.wait_for_element(self.PASSWORD_INPUT).send_keys(password)
        self.wait_for_element(self.COMPANY_INPUT).send_keys(company)
        self.wait_for_element(self.WEBSITE_INPUT).send_keys(website)

        country_elem = self.wait_for_element(self.COUNTRY_DROPDOWN)
        select = Select(country_elem)
        select.select_by_visible_text(country)

        self.wait_for_element(self.CITY_INPUT).send_keys(city)
        self.wait_for_element(self.ADDRESS1_INPUT).send_keys(address1)
        self.wait_for_element(self.ADDRESS2_INPUT).send_keys(address2)
        self.wait_for_element(self.STATE_INPUT).send_keys(state)
        self.wait_for_element(self.ZIP_INPUT).send_keys(zipcode)

    def submit_form(self):
        """Step 57: Clicks the form submit button."""
        btn = self.wait_for_element(self.SUBMIT_BTN)
        self.driver.execute_script("arguments[0].click();", btn)

    def get_success_message(self) -> str:
        """Step 57: Returns the success message displayed upon successful form submission."""
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(
            lambda d: d.find_element(*self.SUCCESS_MSG) if d.find_element(*self.SUCCESS_MSG).text.strip() != "" else False
        )
        return elem.text
