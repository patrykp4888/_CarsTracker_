class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost:5432/users"
    SECRET_KEY = "secretkey"
    DEBUG = True