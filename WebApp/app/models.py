from app import db
from app import bcrypt


class Users(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey('Profiles.profile_id'))

    profiles = db.relationship('Profiles', backref='user')


    def __create_profile(self):
        profile = Profiles()
        db.session.add(profile)
        db.session.commit()
        return profile
    
    def __init__(self, username, password, email, name=None, surname=None):
        self.username = username
        self.name = name
        self.surname = surname
        self.password = bcrypt.generate_password_hash(password)
        self.email = email

        profile = self.__create_profile()
        self.profile_id = profile.profile_id



class Profiles(db.Model):
    __tablename__ = "Profiles"

    profile_id = db.Column(db.Integer, primary_key=True)
    total_searched_cars = db.Column(db.Integer, nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False)
    phone_num_id = db.Column(db.Integer, db.ForeignKey('PhoneNumbers.phone_num_id'))

    phone_numbers = db.relationship('PhoneNumbers', backref='profile')


class PhoneNumbers(db.Model):
    __tablename__ = 'PhoneNumbers'

    phone_num_id = db.Column(db.Integer, primary_key=True)
    phone_num = db.Column(db.Integer, nullable=True)
    country_code = db.Column(db.Integer, nullable=True)