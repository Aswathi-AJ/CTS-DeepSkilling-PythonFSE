# Selenium Basics

This README contains the Selenium automation content for this folder only.

## Overview

This module focuses on browser automation using Python and Selenium.

## Main Areas

- Selenium WebDriver scripts
- Locators and waits
- Page Object Model (POM)
- Pytest-based test execution

## Folder Structure

- automation_scripts
  - Selenium standalone scripts
- pages
  - Page classes for automated test interactions
- tests
  - Pytest test suite

## Setup

```bash
cd SeleniumBasics\Aswathi-AJ
pip install -r requirements.txt
```

## Run Automation Scripts

```bash
python automation_scripts/setup_test.py
python automation_scripts/locators_waits.py
```

## Run Test Suite

```bash
pytest tests\test_pom_suite.py -v --html=tests\report.html --self-contained-html
```

## Notes

This README is limited to Selenium-related content only.
