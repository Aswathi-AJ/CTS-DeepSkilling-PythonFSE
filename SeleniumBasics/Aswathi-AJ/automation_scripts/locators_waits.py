"""
# Task 1: Locator Strategies — From Simple to Robust (Steps 32-35)
# Task 2: WebDriverWait and Expected Conditions (Steps 36-39)

================================================================================
STEP 35: LOCATOR STRATEGY RANKING & JUSTIFICATION (MOST TO LEAST PREFERRED)
================================================================================
1. By.ID:
   - Rank: #1 (Most Preferred)
   - Why: IDs are unique per W3C standards, extremely fast, readable, and highly resistant to layout changes.
2. By.NAME:
   - Rank: #2
   - Why: Usually unique within form scopes, highly readable, standard in form submissions.
3. By.CSS_SELECTOR:
   - Rank: #3
   - Why: Extremely flexible, faster rendering in browser engines, supports classes, attributes, structural hierarchies, and Pseudo-classes.
4. By.XPATH (Relative):
   - Rank: #4
   - Why: Powerful for complex XML/HTML traversal (e.g. searching by inner text, dynamic siblings, parent-axis traversal) when CSS selectors cannot express the condition.
5. By.CLASS_NAME / By.TAG_NAME:
   - Rank: #5
   - Why: Often non-unique (shared across multiple elements); prone to returning wrong element unless qualified.
6. By.XPATH (Absolute):
   - Rank: #6 (Least Preferred - ANTI-PATTERN)
   - Why: E.g., '/html/body/div[2]/div[1]/form/div/input'. Extremely brittle; any tiny DOM wrapper change breaks the locator completely.
================================================================================
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from webdriver_manager.chrome import ChromeDriverManager


def run_locators_and_waits_demo():
    print("=== Running Hands-On 5: Locators & Explicit Waits ===")

    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # ----------------------------------------------------------------------
        # STEP 32 & 33: 6 Locator Strategies & 3 CSS Selector Patterns
        # ----------------------------------------------------------------------
        print("\n--- [Task 1] Testing 6 Locator Strategies & CSS Patterns ---")
        driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

        # 1. By.ID
        elem_id = driver.find_element(By.ID, "user-message")
        print(f"[Step 32] By.ID located element placeholder: '{elem_id.get_attribute('placeholder')}'")

        # 2. By.CLASS_NAME
        elem_class = driver.find_elements(By.CLASS_NAME, "form-control")[0]
        print(f"[Step 32] By.CLASS_NAME located element: {elem_class.tag_name}")

        # 3. By.TAG_NAME
        elem_tag = driver.find_elements(By.TAG_NAME, "input")[0]
        print(f"[Step 32] By.TAG_NAME located input element")

        # 4. By.XPATH (Absolute)
        elem_xpath_abs = driver.find_element(By.XPATH, "/html/body/div[1]//input[@id='user-message']")
        print(f"[Step 32] By.XPATH (Absolute) located element successfully")

        # 5. By.XPATH (Relative)
        elem_xpath_rel = driver.find_element(By.XPATH, "//input[@id='user-message']")
        print(f"[Step 32] By.XPATH (Relative) located element: id='{elem_xpath_rel.get_attribute('id')}'")

        # ----------------------------------------------------------------------
        # STEP 33: 3 CSS Selector Patterns for the Same Element
        # ----------------------------------------------------------------------
        # Pattern 1: By ID (#id)
        css_id = driver.find_element(By.CSS_SELECTOR, "#user-message")
        # Pattern 2: By Attribute ([name='value'])
        css_attr = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Please enter your Message']")
        # Pattern 3: By Parent-Child Relationship (div > input)
        css_parent_child = driver.find_element(By.CSS_SELECTOR, "div > input#user-message")
        print(f"[Step 33] CSS Selectors (ID, Attr, Parent-Child) successfully verified.")

        # ----------------------------------------------------------------------
        # STEP 34: Checkbox Demo - XPath text() and contains()
        # ----------------------------------------------------------------------
        print("\n--- [Step 34] Checkbox Demo XPath text() and contains() ---")
        driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")

        # XPath with text()
        label_text = driver.find_element(By.XPATH, "//label[text()='Click on check box']")
        print(f"[Step 34] XPath text() matched label: '{label_text.text}'")

        # XPath with contains()
        option_labels = driver.find_elements(By.XPATH, "//label[contains(text(),'Option')]")
        print(f"[Step 34] XPath contains() found {len(option_labels)} option labels.")
        for idx, lbl in enumerate(option_labels, 1):
            print(f"  Option Label {idx}: '{lbl.text}'")

        # ----------------------------------------------------------------------
        # STEP 36 & 37: Bootstrap Alerts Explicit Wait vs Hardcoded Sleep
        # ----------------------------------------------------------------------
        print("\n--- [Task 2] Bootstrap Alerts Explicit Wait vs Hardcoded Sleep ---")
        driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

        # Click Normal Success Message button
        success_btn = driver.find_element(By.CSS_SELECTOR, "button.btn-success")
        
        # --- Timing Sleep(3) ---
        start_sleep = time.time()
        success_btn.click()
        time.sleep(3)  # Hardcoded sleep
        alert_sleep = driver.find_element(By.CSS_SELECTOR, ".alert-success")
        time_sleep_taken = time.time() - start_sleep
        print(f"[Step 37] Hardcoded time.sleep(3) execution time: {time_sleep_taken:.4f} seconds")

        # --- Timing Explicit Wait ---
        start_explicit = time.time()
        wait = WebDriverWait(driver, 10)
        success_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-success")))
        success_btn.click()
        alert_explicit = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
        time_explicit_taken = time.time() - start_explicit
        print(f"[Step 37] Explicit WebDriverWait execution time: {time_explicit_taken:.4f} seconds")
        print(f"[Step 36] Alert Text verified: '{alert_explicit.text.strip()}'")
        assert len(alert_explicit.text.strip()) > 0, "Alert text was empty"

        """
        COMMENT ON SLEEP VS EXPLICIT WAIT DIFFERENCE:
        - time.sleep(3) forces the execution thread to freeze for the full 3 seconds regardless of how fast
          the element renders (e.g. rendered in 10ms but wasted 2990ms).
        - WebDriverWait polls the DOM dynamically and returns as soon as the condition is satisfied (e.g. 50ms),
          making test execution significantly faster on high-speed machines while remaining resilient on slow servers.
        """

        # ----------------------------------------------------------------------
        # STEP 38: EC.element_to_be_clickable() Demonstration
        # ----------------------------------------------------------------------
        print("\n--- [Step 38] Demonstrating EC.element_to_be_clickable() ---")
        clickable_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-success")))
        print(f"[Step 38] Button is clickable: '{clickable_btn.text}'")

        """
        DIFFERENCE BETWEEN visibility_of_element_located VS element_to_be_clickable:
        1. visibility_of_element_located checks that the element is present in DOM AND has a width/height greater than 0
           and is not set to display:none or visibility:hidden.
        2. element_to_be_clickable checks visibility AND that the element is enabled (is_enabled() == True)
           AND is not obscured by overlay spinners, modals, or pointer-events: none.
        """

        # ----------------------------------------------------------------------
        # STEP 39: FluentWait Demonstration (Custom Polling & Ignored Exceptions)
        # ----------------------------------------------------------------------
        print("\n--- [Step 39] Demonstrating FluentWait ---")
        driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

        # FluentWait setup in Python using WebDriverWait parameters
        fluent_wait = WebDriverWait(
            driver,
            timeout=10,
            poll_frequency=0.5,  # Poll every 500 milliseconds
            ignored_exceptions=[NoSuchElementException, ElementNotInteractableException]
        )

        table_row = fluent_wait.until(
            EC.presence_of_element_located((By.XPATH, "//table[@id='example']//tbody//tr[1]"))
        )
        print(f"[Step 39] FluentWait successfully located first table row: '{table_row.text[:40]}...'")

    finally:
        driver.quit()
        print("[Step 32-39] Locators & Waits test run complete.")


if __name__ == "__main__":
    run_locators_and_waits_demo()
