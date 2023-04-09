from wtforms import (
    StringField,
    IntegerField,
    PasswordField,
    EmailField,
    SelectField,
    validators,
)
from flask_wtf import FlaskForm
from datetime import date

from .models.cars import Brands, Models


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


class LoginForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])


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

    # def __init__(self):
    #     super().__init__()
    #     self.brand.choices = [
    #         (brand.brand_id, brand.brand) for brand in Brands.query.all()
    #     ]
    #     self.model.choices = [
    #         (model.model_id, model.model) for model in Models.query.all()
    #     ]
