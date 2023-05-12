# import os

# class Config:
#     SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"] # "postgresql://postgres:admin@localhost:5432/users"
#     SECRET_KEY = os.environ["SECRET_KEY"]


class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@db:5432/cars_tracker"
    SECRET_KEY = "secretkey"
