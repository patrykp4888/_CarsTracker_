from wtforms import (
    StringField,
    IntegerField,
    BooleanField,
    PasswordField,
    EmailField,
    SelectField,
    HiddenField,
    validators,
)
from flask_wtf import FlaskForm
from datetime import date


class RegisterForm(FlaskForm):
    username = StringField(
        "Username", [validators.Length(min=4, max=100), validators.DataRequired()]
    )
    email = EmailField(
        "Email", [validators.Length(min=6, max=120), validators.DataRequired()]
    )
    password = PasswordField(
        "Password",
        [
            validators.DataRequired(),
            validators.EqualTo("confirm_password", message="Password must match!"),
        ],
    )
    confirm_password = PasswordField("Repeat password")
    csrf_token = HiddenField()

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])
    remember_me = BooleanField("Remember me", [validators.Optional()])
    csrf_token = HiddenField()


class ProfileForm(FlaskForm):
    username = StringField("New username")
    email = EmailField("New email")
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    csrf_token = HiddenField()


class PasswordForm(FlaskForm):
    old_password = StringField("Old Password")
    new_password = StringField("New Password")
    confirm_new_password = StringField("Confirm New Password")
    csrf_token = HiddenField()


class CarSearchForm(FlaskForm):
    brand = SelectField("Brand", [validators.DataRequired()])
    model = SelectField("Model", [validators.DataRequired()])
    min_production_year = IntegerField(
        "Minimal Production Year",
        [
            validators.DataRequired(),
            validators.NumberRange(min=1900, max=int(date.today().year)),
        ],
    )
    max_production_year = IntegerField(
        "Maximal Production Year",
        [
            validators.DataRequired(),
            validators.NumberRange(min=1900, max=int(date.today().year)),
        ],
    )
    min_mileage = IntegerField(
        "Minimal Mileage",
        [validators.DataRequired(), validators.NumberRange(min=0, max=2_000_000)],
    )
    max_mileage = IntegerField(
        "Maximal Mileage",
        [validators.DataRequired(), validators.NumberRange(min=0, max=2_000_000)],
    )
    csrf_token = HiddenField()

