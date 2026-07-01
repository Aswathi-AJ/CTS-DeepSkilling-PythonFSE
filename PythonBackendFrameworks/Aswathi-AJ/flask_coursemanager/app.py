from flask import Flask
from config import Config
from courses.routes import courses_bp
from courses import db
from flask_migrate import Migrate
from courses.models import Department, Course, Student, Enrollment

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(courses_bp)

    @app.errorhandler(404)
    def not_found(error):
        return {
            "success": False,
            "message": "Resource not found"
        }, 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return {
            "success": False,
            "message": "Internal Server Error"
        }, 500

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)