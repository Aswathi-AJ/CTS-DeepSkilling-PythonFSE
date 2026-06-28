from flask import Blueprint, jsonify, request


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

# Temporary in-memory storage
courses = []


@courses_bp.route("/", methods=["GET"])
def get_courses():
    return api_response(
        True,
        "Courses retrieved successfully",
        courses,
        200
    )


@courses_bp.route("/", methods=["POST"])
def add_course():
    data = request.get_json()
    required_fields = [
        "name",
        "code",
        "credits"
    ]
    for field in required_fields:
        if field not in data:
            return api_response(
                False,
                f"{field} is required",
                None,
                400
            )
    data["id"] = len(courses) + 1
    courses.append(data)
    return api_response(
        True,
        "Course created successfully",
        data,
        201
    )


@courses_bp.route("/<int:course_id>", methods=["GET"])
def get_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            return api_response(
                True,
                "Course retrieved successfully",
                course,
                200
            )
    return api_response(
        False,
        "Course not found",
        None,
        404
    )


@courses_bp.route("/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    data = request.get_json()
    for course in courses:
        if course["id"] == course_id:
            course.update(data)
            return api_response(
                True,
                "Course updated successfully",
                course,
                200
            )
    return api_response(
        False,
        "Course not found",
        None,
        404
    )


@courses_bp.route("/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            courses.remove(course)
            return api_response(
                True,
                "Course deleted successfully",
                None,
                200
            )
    return api_response(
        False,
        "Course not found",
        None,
        404
    )