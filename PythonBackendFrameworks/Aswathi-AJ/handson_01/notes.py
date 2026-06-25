"""
Task 1 

Question 1

Request-Response Cycle:

Browser
   |
GET /api/courses/
   |
URL Router (urls.py)
   |
View (views.py)
   |
Model (models.py)
   |
Database
   |
Model
   |
View
   |
HTTP Response
   |
Browser


Question 2

Middleware is a layer between the browser and the Django application.
Every request passes through middleware before reaching the View.
Every response also passes through middleware before returning to the browser.

Flow:
Browser
   |
Middleware
   |
URL Router
   |
View
   |
Model
   |
Database

Two Built-in Middleware:

1. SecurityMiddleware
   - Adds security-related HTTP headers.
   - Helps protect the application from common attacks.
2. SessionMiddleware
   - Handles user sessions.
   - Keeps users logged in across multiple requests.

   
Question 3

WSGI (Web Server Gateway Interface)
- Handles synchronous requests.
- Processes one request at a time.
- Used for traditional web applications.

ASGI (Asynchronous Server Gateway Interface)
- Handles asynchronous requests.
- Can process multiple requests concurrently.
- Supports WebSockets, live notifications, and real-time applications.

Django uses WSGI by default.
ASGI is preferred for applications that require real-time communication such as chat systems and live updates.


Question 4

MVC stands for Model-View-Controller.
Model:Handles data and database operations.
View:Displays data to the user.
Controller:Handles requests and business logic.

Django follows the MVT architecture.
MVT Mapping:
MVC                  Django (MVT)
---------------------------------------------
Model          -->   Model
View           -->   Template
Controller     -->   View
"""

"""
Task 2

Question 5

Project Files:
1. manage.py - Command-line utility used to manage the Django project.
2. settings.py - Stores project configurations such as installed apps, database, middleware, and security settings.
3. urls.py - Maps incoming URLs to the appropriate view functions.
4. wsgi.py - Entry point for deploying Django applications using WSGI servers.
5. asgi.py - Entry point for deploying Django applications using ASGI servers.


Question 6

Django Project:
- A complete web application.
- Contains project settings, URLs, and configuration.
- Can include multiple Django apps.
Django App:
- A reusable module that performs a specific function.
- Contains its own models, views, admin, and tests.
- Multiple apps can exist inside a single Django project.


Question 7

Registering the App:The courses app must be added to INSTALLED_APPS in settings.py so that Django recognizes it.
Example:
INSTALLED_APPS = [
    ...
    'courses.apps.CoursesConfig',
]

Purpose:
- Enables Django to detect the app.
- Loads models, templates, and migrations.
- Allows the app to participate in the project.


Question 8

A View handles incoming HTTP requests and returns HTTP responses.
Example:

from django.http import HttpResponse
def hello_view(request):
    return HttpResponse("Course Management API is running")

    
Question 9

The include() function is used to delegate URL handling to an application's urls.py file.
Main URL:
path("api/", include("courses.urls"))
courses/urls.py:
path("hello/", hello_view)

Final URL:
http://127.0.0.1:8000/api/hello/


Question 10

The Django development server is started using python manage.py runserver
Opening http://127.0.0.1:8000/api/hello/
returns: Course Management API is running

This confirms that URL routing and the View are working correctly.
"""