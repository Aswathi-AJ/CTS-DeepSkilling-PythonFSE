from . import db
from flask import Blueprint, jsonify, request
from courses.models import Course

def api_response(success, message, data=None, status_code=200):
    response = {
        "success": success,
        "message": message,
        "data": data
    }
    return jsonify(response), status_code


courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)




@courses_bp.route("/", methods=["GET"])
def get_courses():
    courses = Course.query.all()

    result = []

    for course in courses:
        result.append({
            "id": course.id,
            "name": course.name,
            "code": course.code,
            "credits": course.credits,
            "department_id": course.department_id
        })

    return jsonify(result), 200


@courses_bp.route("/", methods=["POST"])
def add_course():

    data = request.get_json()

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"],
        department_id=data["department_id"]
    )

    db.session.add(course)
    db.session.commit()

    return jsonify({
        "message": "Course added successfully"
    }), 201


@courses_bp.route("/<int:course_id>", methods=["GET"])
def get_course(course_id):

    course = Course.query.get(course_id)

    if not course:
        return jsonify({"message": "Course not found"}), 404

    return jsonify({
        "id": course.id,
        "name": course.name,
        "code": course.code,
        "credits": course.credits,
        "department_id": course.department_id
    }), 200


@courses_bp.route("/<int:course_id>", methods=["PUT"])
def update_course(course_id):

    course = Course.query.get(course_id)

    if not course:
        return jsonify({"message": "Course not found"}), 404

    data = request.get_json()

    course.name = data["name"]
    course.code = data["code"]
    course.credits = data["credits"]
    course.department_id = data["department_id"]

    db.session.commit()

    return jsonify({
        "message": "Course updated successfully"
    }), 200


@courses_bp.route("/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):

    course = Course.query.get(course_id)

    if not course:
        return jsonify({"message": "Course not found"}), 404

    db.session.delete(course)
    db.session.commit()

    return jsonify({
        "message": "Course deleted successfully"
    }), 200