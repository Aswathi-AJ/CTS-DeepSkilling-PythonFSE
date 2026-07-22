<!-- Task 1: Map Testing Types to a Real System (Steps 1-4) -->
# Hands-On 1: QA Concepts, Functional Testing & Defect Lifecycle

## Task 1: Map Testing Types to a Real System

### Step 1: Concrete Test Cases by Testing Level (Course Management API)

1. **Unit Testing**
   - **Target**: Testing an isolated utility function in the backend module (e.g., `validate_course_code(code)`).
   - **Test Case**: Verify that `validate_course_code("CS101")` returns `True` and `validate_course_code("INVALID-12345")` returns `False`.
   - **Isolation**: Executed in isolation using mock inputs without starting the HTTP server or connecting to the database.

2. **Integration Testing**
   - **Target**: Testing the interaction between the Course API Router layer and the Database Repository layer.
   - **Test Case**: Execute a service layer method `CourseService.create_course(course_data)` and verify that a record is successfully written to the PostgreSQL database table `courses` and the returned object matches the inserted payload.

3. **System Testing**
   - **Target**: End-to-end evaluation of the full Course Management System.
   - **Test Case**: Send an HTTP POST request to `/api/courses/` via API client, verify authentication token validation, database entry creation, event log publishing to Kafka/RabbitMQ, and an HTTP 201 Created response payload return.

4. **User Acceptance Testing (UAT)**
   - **Target**: Evaluated from the perspective of an actual College Administrator.
   - **Test Case**: A College Admin logs in to the portal, navigates to "Manage Courses", submits a form to add "Advanced Machine Learning (CS402)", assigns an instructor, and verifies the new course is immediately visible to enrolled students.

---

### Step 2: Functional vs Non-Functional Classification & Example

- **Unit Test Case**: Functional (validates correct logic of course code validation rule).
- **Integration Test Case**: Functional (validates data transaction between service and database).
- **System Test Case**: Functional (validates API workflow and contract compliance).
- **UAT Test Case**: Functional (validates business workflow satisfaction).

#### Non-Functional Test Case Example (Performance / Load Testing)
- **Title**: API Endpoint Response Time Under Concurrent Load
- **Description**: Send 500 concurrent `GET /api/courses/` requests within 1 second using Locust/JMeter.
- **Expected Outcome**: 95% of requests return HTTP 200 within <= 200 ms, with 0% error rate and CPU utilization below 80%.

---

### Step 3: Black-Box vs White-Box Testing

- **Black-Box Testing**: Testing the application's functionality without any knowledge of its internal code structure, implementation details, or source code. The tester interacts solely through inputs and inspects outputs (e.g., UI or REST API endpoints).
- **White-Box Testing**: Testing with full access and visibility into internal source code, algorithms, and architecture. Tests focus on code coverage, branch coverage, control flow, and data flow.
- **Roles & Responsibilities**:
  - **QA Testers** primarily perform **Black-Box** (and **Gray-Box**) testing to validate system behavior against user requirements.
  - **Software Developers** primarily perform **White-Box** testing when writing unit and component integration tests.

---

### Step 4: Formal Test Cases for `POST /api/courses/` Endpoint

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_API_001** | Verify successful creation of a new course with valid details. | Admin user is authenticated; valid Auth Token available. | 1. Send `POST /api/courses/` with header `Authorization: Bearer <token>` and body `{"code": "CS101", "name": "Python Programming", "credits": 4}`.<br>2. Inspect HTTP status code and response body. | HTTP Status 201 Created; Body contains assigned `id` and matching course fields. | | |
| **TC_API_002** | Verify request fails when duplicate course code is submitted. | Course with code `CS101` already exists in database. | 1. Send `POST /api/courses/` with body `{"code": "CS101", "name": "Duplicate Python", "credits": 3}`.<br>2. Inspect HTTP status code and error message. | HTTP Status 409 Conflict; Body contains error message: "Course code CS101 already exists". | | |
| **TC_API_003** | Verify validation error when mandatory field `name` is missing. | Admin user is authenticated. | 1. Send `POST /api/courses/` with body `{"code": "CS102", "credits": 4}`.<br>2. Inspect response. | HTTP Status 400 Bad Request; Response validation error lists `name` as required field. | | |

---

<!-- Task 2: Defect Lifecycle & Severity Classification (Steps 5-8) -->
## Task 2: Defect Lifecycle & Severity Classification

### Step 5: Complete Defect Lifecycle Workflow

#### ASCII Lifecycle Diagram
```text
  +---------+      Assign       +----------+      Develop       +--------+
  |   NEW   | ----------------> | ASSIGNED | -----------------> |  OPEN  |
  +---------+                   +----------+                    +--------+
       |                             |                              |
       | Reject                      | Defer                        | Fix
       v                             v                              v
  +----------+                  +----------+                    +--------+
  | REJECTED |                  | DEFERRED |                    | FIXED  |
  +----------+                  +----------+                    +--------+
                                                                    |
                                                                    | Re-test
                                                                    v
                                  +--------+     Verification   +--------+
                                  | CLOSED | <----------------- | RETEST |
                                  +--------+       Passed       +--------+
                                                                    |
                                                                    | Verification Failed
                                                                    v
                                                              +------------+
                                                              | RE-OPENED  |
                                                              +------------+
                                                                    | (Back to OPEN)
```

#### Defect States Description
1. **NEW**: Defect logged by QA tester for the first time.
2. **ASSIGNED**: Lead/Manager assigns the defect to a developer for resolution.
3. **OPEN**: Developer starts analyzing and working on the bug fix.
4. **FIXED**: Developer completes code fix and deploys to test environment.
5. **RETEST**: QA tests the fix in the updated build.
6. **VERIFIED**: QA confirms bug is fixed and no regression occurred.
7. **CLOSED**: Defect is officially resolved and archived.
8. **REJECTED**: Bug is invalidated (not a bug, duplicate, or working as designed).
9. **DEFERRED**: Fix postponed to a future sprint/release due to priority or low impact.
10. **RE-OPENED**: Bug persists during retesting and is returned to developer.

---

### Step 6: Severity & Priority Classification Matrix

| Bug Scenario | Severity | Priority | Justification |
| :--- | :--- | :--- | :--- |
| **a) `POST /api/courses/` returns 500 Internal Server Error for all requests.** | **Critical** | **P1** | **Severity**: Core business functionality is completely broken for all users without any workaround.<br>**Priority**: Requires immediate hotfix as course creation is blocked. |
| **b) Course names longer than 150 characters are silently truncated without an error.** | **Medium** | **P3** | **Severity**: Data integrity issue but affects rare edge-case long titles without crashing the application.<br>**Priority**: Needs fixing in regular release cycle. |
| **c) The `/docs` Swagger page has a typo in the API description.** | **Low** | **P4** | **Severity**: Cosmetic documentation flaw; zero functional impact.<br>**Priority**: Fix when time permits in minor update. |
| **d) Login with correct credentials occasionally returns 401 on the first attempt (intermittent).** | **High** | **P2** | **Severity**: User login fails intermittently, creating poor UX and suggesting race conditions/session storage bugs.<br>**Priority**: High priority to investigate root cause before production launch. |

---

### Step 7: Complete Defect Report for Bug (a)

```text
================================================================================
DEFECT REPORT: DEF-2026-001
================================================================================
Defect ID       : DEF-2026-001
Title           : POST /api/courses/ returns 500 Internal Server Error for all valid payloads
Environment     : Staging Environment (v1.4.0-rc2)
Build Version   : Build 2026.07.20-101
Severity        : Critical
Priority        : P1 (Immediate)
Reporter        : Aswathi AJ (QA Engineer)
Assigned To     : Backend Lead Developer

--------------------------------------------------------------------------------
STEPS TO REPRODUCE:
1. Launch Postman or cURL terminal.
2. Set header: Authorization: Bearer <valid_admin_jwt>
3. Set header: Content-Type: application/json
4. Send POST request to http://staging.api.college.edu/api/courses/ with body:
   {
     "code": "CS201",
     "name": "Data Structures",
     "credits": 4
   }
5. Observe response status code and body.

EXPECTED RESULT:
- HTTP Status Code: 201 Created
- Response Body: JSON object containing course details and created ID.

ACTUAL RESULT:
- HTTP Status Code: 500 Internal Server Error
- Response Body: {"detail": "Internal Server Error: ConnectionPool timeout on PostgreSQL"}

ATTACHMENTS:
- Screenshot: screenshot_500_error.png (showing Postman 500 response & server log stack trace)
================================================================================
```

---

### Step 8: Severity vs Priority Distinction & Real-World Example

- **Severity**: Measures the technical impact of a defect on the system architecture, functionality, or data integrity (determined by QA/Technical Team).
- **Priority**: Measures the urgency with which a defect must be resolved based on business needs, release schedules, or executive visibility (determined by Product Manager/QA Lead).

#### Real-World Example: High Severity with Low Priority
- **Scenario**: A legacy background batch job that runs once a year on December 31st crashes due to an unhandled null pointer exception (500 error).
- **Why High Severity**: System process crashes completely without fallback (High/Critical technical impact).
- **Why Low Priority (P3/P4)**: The issue occurred in January right after the annual run, meaning it will not impact any operational users or business processes for another 11 months. The fix can be scheduled in a sprint later in the year.
