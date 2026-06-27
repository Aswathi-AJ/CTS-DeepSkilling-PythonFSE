class Config:
    SECRET_KEY = "mysecretkey"
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///coursemanager.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False