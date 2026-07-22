<!-- Task 1: V-Model Mapping (Steps 9-12) -->
# Hands-On 2: SDLC vs TDLC — V-Model & Agile QA Integration

## Task 1: V-Model Mapping

### Step 9: The Complete V-Model Architecture

```text
===================================================================================
                         THE V-MODEL TESTING ARCHITECTURE
===================================================================================

  SDLC DEVELOPMENT PHASES (Left)                  TDLC TESTING PHASES (Right)

  +--------------------------+                      +--------------------------+
  |  Requirements Analysis   | <==================> |    Acceptance Testing    |
  +--------------------------+                      +--------------------------+
               \                                                 /
                \                                               /
  +--------------------------+                      +--------------------------+
  |   System Design Specs    | <==================> |      System Testing      |
  +--------------------------+                      +--------------------------+
               \                                                 /
                \                                               /
  +--------------------------+                      +--------------------------+
  |   Architecture Design    | <==================> |   Integration Testing    |
  +--------------------------+                      +--------------------------+
               \                                                 /
                \                                               /
  +--------------------------+                      +--------------------------+
  |  Module / Detailed Design| <==================> |       Unit Testing       |
  +--------------------------+                      +--------------------------+
               \                                                 /
                \                                               /
                 +---------------------------------------------+
                 |            CODING / IMPLEMENTATION          |
                 +---------------------------------------------+
===================================================================================
```

---

### Step 10: Test Artifacts Produced Per SDLC Phase

1. **Requirements Analysis Phase** $\rightarrow$ **Acceptance Test Plan & Scenarios**
   - *Artifact*: Acceptance Test Plan, User Story Acceptance Criteria (Gherkin), UAT Test Matrix.
2. **System Design Phase** $\rightarrow$ **System Test Plan & Test Suite**
   - *Artifact*: System Test Plan, End-to-End Test Cases, Functional & Non-Functional Verification Plan.
3. **Architecture Design Phase** $\rightarrow$ **Integration Test Plan & API Contract Suite**
   - *Artifact*: Integration Test Plan, API Contract Specification (OpenAPI/Swagger tests), DB Schema Integration Suite.
4. **Module / Detailed Design Phase** $\rightarrow$ **Unit Test Cases & Stub/Mock Definitions**
   - *Artifact*: Unit Test Specifications, Test Stubs/Mocks, Code Coverage Targets.

---

### Step 11: Entry & Exit Criteria for All 4 Testing Levels

| Testing Level | Entry Criteria (Prerequisites) | Exit Criteria (Completion Conditions) |
| :--- | :--- | :--- |
| **Unit Testing** | 1. Code compilation successful with zero build errors.<br>2. Unit test cases written & reviewed.<br>3. Developer completed module implementation. | 1. 100% unit tests executed with 100% pass rate.<br>2. Minimum 85% code statement coverage achieved.<br>3. Zero high/critical static code analysis issues. |
| **Integration Testing** | 1. All dependent unit tests passed.<br>2. API modules deployed to Integration environment.<br>3. Test database seeded with baseline test data. | 1. All API endpoints & database integration flows executed.<br>2. 0 Critical or High severity defects open.<br>3. Data integrity across database transactions verified. |
| **System Testing** | 1. Integration testing successfully completed & signed off.<br>2. Full build deployed to Staging environment.<br>3. System Test Plan & test data ready. | 1. 100% planned system test cases executed.<br>2. 98%+ pass rate across all functional scenarios.<br>3. Non-functional performance/security SLA requirements met. |
| **Acceptance Testing (UAT)** | 1. System testing signed off by QA lead.<br>2. UAT environment configured with production-like data.<br>3. User Acceptance Test Suite approved by Product Owner. | 1. Key business stakeholders execute UAT scenarios.<br>2. 100% business-critical workflows passed.<br>3. Product Owner signs off for production deployment. |

---

### Step 12: Early QA Engagement Points in V-Model (Course Management API)

1. **Requirements Review Phase (Left Side Top)**:
   - QA actively reviews the Course Management API user stories before coding starts. By identifying missing validation rules (e.g., maximum course length, allowed credit range) early, QA prevents ambiguity defects from entering code.
2. **Architecture Design Review Phase (Left Side Middle)**:
   - QA reviews API endpoint specifications (Swagger/OpenAPI schemas) and database relation diagrams. QA verifies error response codes, rate limiting strategies, and authentication middleware design before implementation.

---

<!-- Task 2: Agile QA and Shift-Left Testing (Steps 13-16) -->
## Task 2: Agile QA and Shift-Left Testing

### Step 13: Problems Caused by Waterfall Testing Model

1. **Late Defect Discovery & High Fix Cost**: Defects introduced during requirements or initial design are only discovered weeks later during system testing, making fixes exponentially more expensive and disruptive.
2. **Testing Compression / Time Crunch**: When development delays occur, the release deadline remains fixed, forcing QA testing schedules to be cut short and increasing operational risk.
3. **Lack of Feedback Loops**: Developers receive feedback long after code is written, leading to lost context and slower bug resolution cycles.

---

### Step 14: QA Engineer Roles Across 4 Agile Ceremonies

1. **Sprint Planning**:
   - QA helps refine user stories by defining clear Acceptance Criteria in Given-When-Then format, identifying edge cases, estimating QA effort, and ensuring stories are testable before commitment.
2. **Daily Standup**:
   - QA communicates testing progress, highlights blockers (e.g., environment issues, blocked API endpoints), and collaborates with developers on resolved defect re-testing.
3. **Sprint Review (Demo)**:
   - QA validates the working product increment against acceptance criteria during the live demo and provides feedback from end-user perspective.
4. **Retrospective**:
   - QA provides insights into sprint quality, analyzes defect trends, proposes process improvements (e.g., adding automated regression tests), and promotes quality ownership.

---

### Step 15: 4 Shift-Left Practices Applied to Course Management API

1. **Reviewing Requirements for Testability**:
   - QA evaluates user story "Add Course" and ensures quantifiable acceptance criteria (e.g., "Course code must be 5-10 alphanumeric characters").
2. **Writing Test Cases Before Code (TDD / BDD)**:
   - QA writes executable Gherkin feature files or pytest unit/integration test skeletons prior to backend feature implementation.
3. **Static Code Analysis**:
   - Automated SonarQube/Flake8 analysis integrated into CI/CD pipelines to catch bugs, security vulnerabilities, and code smells on every git push.
4. **API Contract Testing Before Integration**:
   - Using OpenAPI/Pact schema validation tools to verify API request/response structures between frontend and backend before full feature completion.

---

### Step 16: Given-When-Then (Gherkin) Acceptance Criteria

```gherkin
Feature: Create New Course
  As a college admin
  I want to create a new course
  So that students can enroll in it

  # Scenario 1: Happy Path
  Scenario: Successfully create a new course with valid details
    Given the college admin is logged in with valid credentials
    And the course code "CS101" does not exist in the catalog
    When the admin submits a new course with code "CS101", name "Python Programming", and credits 4
    Then the response status code should be 201 Created
    And the response body should contain the course ID and code "CS101"
    And the new course "CS101" should be stored in the database

  # Scenario 2: Duplicate Course Code
  Scenario: Fail to create a course with an existing course code
    Given the college admin is logged in with valid credentials
    And a course with code "CS101" already exists in the catalog
    When the admin submits a new course with code "CS101", name "Advanced Python", and credits 3
    Then the response status code should be 409 Conflict
    And the error message should state "Course code CS101 already exists"

  # Scenario 3: Missing Required Fields
  Scenario: Fail to create a course when mandatory fields are missing
    Given the college admin is logged in with valid credentials
    When the admin submits a new course without providing the mandatory "name" field
    Then the response status code should be 400 Bad Request
    And the response error details should list "name" as a required field
```
