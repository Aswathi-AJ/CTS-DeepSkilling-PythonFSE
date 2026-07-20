# Hands-On 10 – Microservices Architecture

## Question 96
### Proposed Microservices

| Service Name | Responsibility |
|--------------|----------------|
| Course Service | Manage course creation, update, deletion, and retrieval. |
| Student Service | Manage student registration and student information. |
| Enrollment Service | Handle student enrollments and course registrations. |
| Authentication Service | Manage user registration, login, JWT authentication, and authorization. |

## Question 97
### Microservice Folder Structure

- course_service → Handles course management.
- student_service → Handles student management.
- enrollment_service → Handles student enrollments.
- auth_service → Handles user registration, login, and JWT authentication.
- gateway → Routes client requests to the appropriate microservice.

## Question 98
### API Endpoint Distribution

#### Course Service
- GET /api/v1/courses
- GET /api/v1/courses/{id}
- POST /api/v1/courses
- PUT /api/v1/courses/{id}
- PATCH /api/v1/courses/{id}
- DELETE /api/v1/courses/{id}

#### Student Service
- GET /api/v1/students
- GET /api/v1/students/{id}
- POST /api/v1/students
- PUT /api/v1/students/{id}
- DELETE /api/v1/students/{id}

#### Enrollment Service
- GET /api/v1/enrollments
- POST /api/v1/enrollments
- DELETE /api/v1/enrollments/{id}

#### Authentication Service
- POST /api/v1/auth/register
- POST /api/v1/auth/login

## Question 104

## Synchronous vs Asynchronous Communication

### Synchronous (HTTP)
- Services communicate directly using HTTP requests.
- The caller waits for a response.
- Easy to implement and suitable for real-time operations.
- If one service is down, the other service is affected.
### Asynchronous (Message Queue)
- Services communicate through a message broker (RabbitMQ or Kafka).
- The sender does not wait for an immediate response.
- More scalable and fault tolerant.
- Best for background processing and event-driven systems.

### When to use RabbitMQ or Kafka?
Use RabbitMQ or Kafka for:
- Order processing
- Email notifications
- Logging and analytics
- High-volume or event-driven applications
