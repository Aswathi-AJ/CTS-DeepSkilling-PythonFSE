from fastapi import FastAPI, Depends, HTTPException
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from schemas import CourseCreate, CourseResponse, CourseUpdate
from database import get_db
from models import Course

app = FastAPI(
    title="Course Management API",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI Course Management API"
    }


@app.get(
    "/api/courses/{course_id}",
    response_model=CourseResponse
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
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )
    return course

@app.get("/api/courses/", response_model=list[CourseResponse])
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Course)
    if department_id is not None:
        query = query.where(
            Course.department_id == department_id
        )
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

@app.get("/api/database")
async def database_demo(
    db: AsyncSession = Depends(get_db)
):
    return {
        "message": "Database Connected Successfully"
    }


@app.post("/api/courses/", response_model=CourseResponse)
async def create_course(
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
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
    return new_course

@app.put(
    "/api/courses/{course_id}",
    response_model=CourseResponse
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
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )
    data = updated.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(course, key, value)
    await db.commit()
    await db.refresh(course)
    return course

@app.delete("/api/courses/{course_id}")
async def delete_course(
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
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )
    await db.delete(course)
    await db.commit()
    return {
        "message": "Course deleted successfully"
    }