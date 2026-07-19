from flask import Blueprint, jsonify, request

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)

# Temporary in-memory storage
courses = []

@courses_bp.route("/", methods=["GET"])
def get_courses():
    return jsonify(courses), 200


@courses_bp.route("/", methods=["POST"])
def add_course():
    data = request.get_json()
    courses.append(data)
    return jsonify(data), 201