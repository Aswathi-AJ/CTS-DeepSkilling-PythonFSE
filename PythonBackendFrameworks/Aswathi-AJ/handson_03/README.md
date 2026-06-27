# Hands-On 03 – Django REST Views, URL Routing & Forms

## Objective
Implemented REST APIs for the Course Management System using Django REST Framework (DRF).

## Topics Covered
- Django REST Framework (DRF)
- ModelSerializer
- Functionality of APIView
- ModelViewSet
- URL Routing using DefaultRouter
- CRUD APIs (GET, POST, PUT, DELETE)
- Custom Actions using @action
- Request and Response handling
- Testing APIs using Postman

## Tasks Completed

### Task 1
- Created ModelSerializers for all models.
- Implemented Course List API (GET, POST).
- Implemented Course Detail API (GET, PUT, DELETE).
- Configured URL routing.
- Tested APIs using Postman.

### Task 2
- Refactored APIViews into ModelViewSet.
- Configured DefaultRouter.
- Created ViewSets for Course, Student and Enrollment.
- Added custom `students` action to CourseViewSet.
- Tested router-generated endpoints.

## API Endpoints

- GET /api/courses/
- POST /api/courses/
- GET /api/courses/{id}/
- PUT /api/courses/{id}/
- DELETE /api/courses/{id}/
- GET /api/courses/{id}/students/

## Tools Used

- Python
- Django
- Django REST Framework
- SQLite
- Postman