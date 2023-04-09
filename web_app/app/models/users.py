from flask_login import UserMixin
import datetime

from app import db, bcrypt


class Users(db.Model, UserMixin):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    surname = db.Column(db.String(100), nullable=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey("Profiles.profile_id"))

    profiles = db.relationship("Profiles", backref="user")

    def __create_profile(self):
        profile = Profiles()
        db.session.add(profile)
        db.session.commit()
        return profile

    def __init__(self, username, password, email, name=None, surname=None):
        self.username = username
        self.name = name
        self.surname = surname
        self.password = (bcrypt.generate_password_hash(password)).decode(
            "utf-8", "ignore"
        )
        self.email = email

        profile = self.__create_profile()
        self.profile_id = profile.profile_id


class Profiles(db.Model):
    __tablename__ = "Profiles"

    profile_id = db.Column(db.Integer, primary_key=True)
    total_searched_cars = db.Column(db.Integer, nullable=True)
    registration_date = db.Column(db.DateTime, nullable=True)
    phone_num_id = db.Column(db.Integer, db.ForeignKey("PhoneNumbers.phone_num_id"))

    phone_numbers = db.relationship("PhoneNumbers", backref="profile")

    def __create_phone_number_object(self):
        phonenumber = PhoneNumbers()
        db.session.add(phonenumber)
        db.session.commit()
        return phonenumber

    def __init__(
        self, total_searched_cars=0, registration_date=datetime.datetime.now()
    ):
        self.total_searched_cars = total_searched_cars
        self.registration_date = registration_date

        phonenumber = self.__create_phone_number_object()
        self.phone_num_id = phonenumber.phone_num_id


class PhoneNumbers(db.Model):
    __tablename__ = "PhoneNumbers"

    phone_num_id = db.Column(db.Integer, primary_key=True)
    phone_num = db.Column(db.Integer, nullable=True)
    country_code = db.Column(db.Integer, nullable=True)
