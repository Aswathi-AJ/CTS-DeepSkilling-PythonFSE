from fastapi import FastAPI, Depends,status,BackgroundTasks,Response,HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,func
from schemas import CourseCreate, CourseResponse, CourseUpdate, StudentResponse,StudentCreate,EnrollmentCreate,EnrollmentResponse
from database import get_db
from models import Course, Student, Enrollment,User
from schemas import UserCreate, UserResponse,UserLogin
from security import get_password_hash,verify_password,create_access_token,verify_access_token
from sqlalchemy import select
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    email = verify_access_token(token)
    result = await db.execute(
        select(User).where(User.email == email)
    )
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )
    return user

app = FastAPI(
    title="Course Management API",
    description="A REST API for managing courses, students, and enrollments using FastAPI.",
    version="1.0.0",
    contact={
        "name": "Aswathi AJ",
        "email": "aswathi23@gmail.com"
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")

@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI Course Management API"
    }

# Versioning Strategies:
# 1. URL Versioning (used here): /api/v1/courses/
# 2. Header Versioning:
#    Accept: application/vnd.api+json;version=1

@app.get(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,tags=["Courses"]
)
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(
            Course.id == course_id
        )
    )
    course = result.scalar_one_or_none()
    if course is None:
     return JSONResponse(
        status_code=404,
        content={
            "error": {
                "code": "NOT_FOUND",
                "message": f"Course with id {course_id} does not exist",
                "field": None
            }
        }
    )
    return course

@app.get(
    "/api/v1/courses/",
    tags=["Courses"]
)
async def get_courses(
    page: int = 1,
    page_size: int = 5,
    search: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    offset = (page - 1) * page_size
    query = select(Course)
    if search:
        query = query.where(
            (Course.name.ilike(f"%{search}%")) |
            (Course.code.ilike(f"%{search}%"))
        )
    total = await db.execute(
        select(func.count()).select_from(Course)
    )
    count = total.scalar()
    result = await db.execute(
        query.offset(offset).limit(page_size)
    )
    courses = result.scalars().all()
    next_url = None
    previous_url = None
    if offset + page_size < count:
        next_url = f"/api/v1/courses/?page={page+1}&page_size={page_size}"
    if page > 1:
        previous_url = f"/api/v1/courses/?page={page-1}&page_size={page_size}"
    return {
        "count": count,
        "next": next_url,
        "previous": previous_url,
        "results": courses
    }

@app.get("/api/database")
async def database_demo(
    db: AsyncSession = Depends(get_db)
):
    return {
        "message": "Database Connected Successfully"
    }

@app.get(
    "/api/students/",
    response_model=list[StudentResponse],tags=["Students"]
)
async def get_students(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Student)
    )
    return result.scalars().all()

@app.get(
    "/api/enrollments/",
    response_model=list[EnrollmentResponse],tags=["Enrollments"]
)
async def get_enrollments(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Enrollment)
    )
    return result.scalars().all()

@app.post(
    "/api/v1/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create a new course",
    description="Creates a new course by accepting the course name, code, credits, and department ID."
)
async def create_course(
    course: CourseCreate,
    response: Response,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    response.headers["Location"] = f"/api/v1/courses/{new_course.id}"
    return new_course

@app.post(
    "/api/students/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Students"],
    summary="Create a new student",
    description="Creates a new student by accepting the student's first name, last name, and email."
)
async def create_student(
    student: StudentCreate,
    response: Response,
    db: AsyncSession = Depends(get_db)
):
    new_student = Student(
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email
    )
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    return new_student

@app.post(
    "/api/enrollments/",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,tags=["Enrollments"]
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    response: Response, 
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    new_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )
    db.add(new_enrollment)
    await db.commit()
    await db.refresh(new_enrollment)
    background_tasks.add_task(
    send_confirmation_email,
    "student@example.com"
     )
    return new_enrollment

@app.get(
    "/api/v1/courses/{course_id}/students",
    response_model=list[StudentResponse],tags=["Courses"]
)
async def get_course_students(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Student)
        .join(Enrollment)
        .where(Enrollment.course_id == course_id)
    )
    students = result.scalars().all()
    return students

@app.put(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,tags=["Courses"]
)
async def update_course(
    course_id: int,
    updated: CourseUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(
            Course.id == course_id
        )
    )
    course = result.scalar_one_or_none()
    if course is None:
      return JSONResponse(
        status_code=404,
        content={
            "error": {
                "code": "NOT_FOUND",
                "message": f"Course with id {course_id} does not exist",
                "field": None
            }
        }
    )
    data = updated.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(course, key, value)
    await db.commit()
    await db.refresh(course)
    return course

@app.patch(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"],
    summary="Partially update a course"
)
async def patch_course(
    course_id: int,
    updated: CourseUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )
    course = result.scalar_one_or_none()
    if course is None:
       return JSONResponse(
        status_code=404,
        content={
            "error": {
                "code": "NOT_FOUND",
                "message": f"Course with id {course_id} does not exist",
                "field": None
            }
        }
    )
    update_data = updated.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(course, key, value)
    await db.commit()
    await db.refresh(course)
    return course

@app.delete("/api/v1/courses/{course_id}",status_code=status.HTTP_204_NO_CONTENT,tags=["Courses"])
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Course).where(
            Course.id == course_id
        )
    )
    course = result.scalar_one_or_none()
    if course is None:
      return JSONResponse(
        status_code=404,
        content={
            "error": {
                "code": "NOT_FOUND",
                "message": f"Course with id {course_id} does not exist",
                "field": None
            }
        }
    )
    await db.delete(course)
    await db.commit()
    return None


@app.post(
    "/api/v1/auth/register",
    response_model=UserResponse,
    tags=["Authentication"]
)
async def register_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(User).where(User.email == user.email)
    )
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

# qn no:89
# bcrypt is used instead of MD5 or SHA-256 because it adds a unique salt
# and is computationally slow, making password cracking much more difficult.

    new_user = User(
        email=user.email,
        hashed_password=get_password_hash(user.password),
        is_active=True
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

# qn no:90
# Verification:
# The database stores only bcrypt hashed passwords.
# Plain-text passwords are never saved, improving application security.

@app.post(
    "/api/v1/auth/login",
    tags=["Authentication"]
)
async def login(
    form_data:  OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(User).where(User.email == form_data.username)
    )
    db_user = result.scalar_one_or_none()
    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    if not verify_password(
        form_data.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    access_token = create_access_token(
        {"sub": db_user.email}
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

#qn no:95
# OAuth2 Authorization Code Flow:
# 1. User logs in through an Authorization Server.
# 2. Server returns an Authorization Code.
# 3. Client exchanges the code for an Access Token.
# 4. The Access Token is used to access protected APIs securely.