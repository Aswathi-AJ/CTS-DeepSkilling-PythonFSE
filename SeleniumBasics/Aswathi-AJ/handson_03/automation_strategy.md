<!-- Task 1: Automation Decision and Test Case Selection (Steps 17-20) -->
# Hands-On 3: Test Automation Process, Lifecycle & Framework Types

## Task 1: Automation Decision and Test Case Selection

### Step 17: 5 Automation Decision Criteria Applied to `POST /api/courses/`

1. **Repetitiveness & Frequency**:
   - *Criterion*: Is the test executed frequently across multiple builds, sprints, and environments?
   - *Application*: `POST /api/courses/` is a core CRUD endpoint executed in every build verification test and regression suite. **High Candidate**.
2. **Business Risk & Criticality**:
   - *Criterion*: Does failure in this component cause severe business impact or system downtime?
   - *Application*: Course creation is vital for college admin workflows. Failure blocks enrollment. **High Candidate**.
3. **Feasibility & Technical Feasibility**:
   - *Criterion*: Can the test be deterministically automated with stable APIs and low complexity?
   - *Application*: REST API inputs and HTTP 201 response outputs are structured, deterministic, and easy to validate. **High Candidate**.
4. **Data-Driven Requirements**:
   - *Criterion*: Does the scenario require testing with multiple varied parameter sets?
   - *Application*: Testing valid/invalid credit values, special characters in course names benefit from parameterized datasets. **High Candidate**.
5. **UI / Test Stability**:
   - *Criterion*: Is the test subject to constant UI layout redesigns or unstable contracts?
   - *Application*: Backend API schemas are stable and versioned compared to volatile UI layouts. **High Candidate**.

*Conclusion*: The scenario **'Test that POST /api/courses/ endpoint returns 201 with correct course data when valid input is provided'** meets all 5 criteria and is an **ideal candidate for test automation**.

---

### Step 18: Automate vs. Manual Decisions

| Test Scenario | Decision | Justification |
| :--- | :--- | :--- |
| **a) Regression test for all CRUD endpoints after every code change.** | **Automate** | Highly repetitive, run frequently on every build/PR, deterministic output. |
| **b) Exploratory testing of a new search feature.** | **Manual** | Requires human intuition, creative testing, and ad-hoc boundary exploration without fixed step scripts. |
| **c) Performance test: 100 concurrent users calling GET /api/courses/.** | **Automate** | Impossible to simulate 100 concurrent manual human users accurately; requires automated tools (Locust/JMeter). |
| **d) UI test for login form.** | **Automate** | Standard, high-frequency smoke test required before running any downstream user workflow. |
| **e) Verify API documentation (Swagger) is accurate.** | **Manual** | Documentation clarity, formatting, visual layout, and readability require human inspection (though contract linters help). |
| **f) Smoke test: verify API is reachable after deployment.** | **Automate** | Critical deployment verification script executed in CI/CD pipeline right after deployment to give immediate signal. |

---

### Step 19: Test Automation ROI Calculation

- **Definition of Test Automation ROI**: The ratio of net financial/time savings gained from automated test execution compared to the total investment cost required to develop and maintain the automation scripts.

#### Mathematical Calculation
- **Initial Automation Setup Cost**: $C_{auto\_setup} = 4\text{ hours} = 240\text{ minutes}$.
- **Manual Execution Cost per Run**: $C_{manual} = 30\text{ minutes}$.
- **Maintenance Cost per Run (Runs 1 to 10)**: $0\text{ minutes}$.
- **Maintenance Cost per Run (Runs 11 onwards)**: $20\% \times 30\text{ mins} = 6\text{ minutes/run}$.

#### Step-by-Step Cumulative Comparison

| Run Number | Cumulative Manual Time (mins) | Cumulative Automated Time (Setup + Execution + Maint) | Net Savings / Break-Even Status |
| :---: | :---: | :---: | :--- |
| **Run 1** | 30 | 240 + 0 = 240 | -210 mins (Investment phase) |
| **Run 2** | 60 | 240 | -180 mins |
| **Run 4** | 120 | 240 | -120 mins |
| **Run 6** | 180 | 240 | -60 mins |
| **Run 8** | **240** | **240** | **0 mins (EXACT BREAK-EVEN POINT)** |
| **Run 9** | 270 | 240 | +30 mins (Net Profit Begins) |
| **Run 10** | 300 | 240 | +60 mins |
| **Run 11** | 330 | 240 + 6 = 246 | +84 mins |
| **Run 20** | 600 | 240 + (10 × 6) = 300 | +300 mins (5 Hours Saved) |

*Result*: The test automation pays for itself **at exactly the 8th run**.

---

### Step 20: Flaky Test Analysis & Prevention Strategies

- **Definition of Flaky Test**: A test that exhibits non-deterministic behavior — passing and failing on the exact same code base without any actual application changes.
- **Example**: A Selenium script clicks "Submit Course" and immediately checks for the success alert message. On fast machines, it passes. On slow CI/CD servers, the AJAX response takes 500ms, causing `NoSuchElementException`.

#### 3 Prevention Strategies in Selenium
1. **Replace Implicit Waits and Hard-coded `time.sleep()` with Explicit Waits**: Use `WebDriverWait` with `ExpectedConditions.element_to_be_clickable()` or `visibility_of_element_located()`.
2. **Isolate Test Data & Environment State**: Ensure each test creates its own independent test data and cleans up state (e.g., using pytest fixtures with database rollback/teardown).
3. **Implement Automatic Retry Logic**: Use pytest plugins like `pytest-rerunfailures` (`--reruns 2`) to re-execute transient failures before flagging build failure.

---

<!-- Task 2: Compare Automation Framework Types (Steps 21-23) -->
## Task 2: Compare Automation Framework Types

### Step 21: Comparison of 5 Automation Framework Types

| Framework Type | Description | Advantage | Disadvantage | Course Management Example |
| :--- | :--- | :--- | :--- | :--- |
| **1. Linear (Record & Playback)** | Simple procedural scripts recording explicit step-by-step browser commands sequentially without functions. | Fast setup time for quick proof-of-concept scripts. | Hard to maintain; high code duplication; fragile to UI changes. | Recording a quick 1-off check of login form using Selenium IDE. |
| **2. Modular** | Code divided into independent functional modules or functions (e.g., `login()`, `create_course()`). | High code reusability; updates to a module reflect across all tests. | Data is hardcoded inside function scripts. | Creating `login_helper.py` reused across 15 different course tests. |
| **3. Data-Driven** | Test logic is separated from test data. Tests read input parameters and expected results from external CSV/Excel/JSON files. | Allows running the same test script against 100s of data variations easily. | Requires handling external file parsing and error handling. | Parameterizing course creation with 50 course names/codes from `courses.json`. |
| **4. Keyword-Driven** | Actions and keywords (e.g., `Click`, `InputText`, `VerifyText`) are mapped to code, driven by spreadsheets. | Allows non-technical testers to write test cases using spreadsheet keywords. | High initial framework development and maintenance overhead. | Defining keywords like `LOGIN_ADMIN`, `ADD_COURSE` in Excel for QA analysts. |
| **5. Hybrid** | Combines Modular, Data-Driven, Keyword-Driven, and Page Object Model patterns into a unified design. | Highly scalable, maintainable, flexible, and robust for large projects. | Complex initial setup requiring experienced automation architects. | Production-grade Selenium suite using Page Objects + Pytest Parameterization + JSON Data. |

---

### Step 22: Framework Recommendation for Given Scenario

- **Scenario Requirement**: Test login with 50 user/password combinations, reuse login steps across 20 test cases, and support technical & non-technical team members writing tests.
- **Recommended Framework**: **Hybrid Automation Framework (Modular + Data-Driven + BDD / Page Object Model)**.
- **Justification**:
  1. **Data-Driven Component**: Handles the 50 user/password credentials from external CSV/JSON files or `@pytest.mark.parametrize`.
  2. **Modular / POM Component**: Reuses the login page object and steps across 20 downstream test cases without duplicating code.
  3. **BDD / Keyword Component (Behave / Gherkin)**: Enables non-technical members to write scenarios in plain English (Given-When-Then), while technical members implement underlying Python page objects.

---

### Step 23: Hybrid Framework Folder Structure

```text
c:\CTS Deepskilling Python FSE\SeleniumBasics\Aswathi-AJ\
├── config/
│   └── config.ini                # Environment URLs, timeouts, browser settings
├── test_data/
│   └── users_data.json           # External JSON/CSV test data files
├── pages/                        # Page Object Model locators and actions
│   ├── base_page.py
│   ├── login_page.py
│   └── course_page.py
├── utilities/                    # Helper functions (WebDriver factory, Excel/JSON parser, loggers)
│   ├── driver_factory.py
│   └── data_reader.py
├── tests/                        # Test scripts containing assertions
│   ├── conftest.py               # Shared Pytest fixtures
│   ├── test_login.py
│   └── test_course_creation.py
├── reports/                      # Generated HTML execution reports & failure screenshots
│   ├── report.html
│   └── screenshots/
└── requirements.txt              # Dependency management
```
