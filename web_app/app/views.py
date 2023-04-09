from flask import render_template, url_for, redirect, flash, request
from flask.views import View, MethodView
from flask_login import login_user, logout_user, login_required, current_user

from app import db, bcrypt
from .states import UserStates
from .models.users import Users
from .forms import RegisterForm, LoginForm, CarSearchForm


class IndexView(View):
    def dispatch_request(self):
        return render_template("home.html", user=current_user)


class HomeView(View):
    def __create_car_search_form(self):
        return CarSearchForm(request.form)

    def __check_form_validity(self, car_search_form):
        if car_search_form.validate():
            brand = request.form.get("brand")
            model = request.form.get("model")
            min_production_year = request.form.get("min_production_year")
            max_production_year = request.form.get("max_production_year")
            min_mileage = request.form.get("min_mileage")
            max_mileage = request.form.get("max_mileage")
            return f"[OK] RESULTS : {brand, model, min_production_year, max_production_year, min_mileage, max_mileage}"
        else:
            return "[ERROR]"

    def get(self):
        car_search_form = self.__create_car_search_form()
        return render_template(
            "home.html", car_search_form=car_search_form, user=current_user
        )

    def post(self):
        car_search_form = self.__create_car_search_form()
        return self.__check_form_validity(car_search_form=car_search_form)


class RegisterView(MethodView):
    def __register_to_db(self, register_form):
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data

        existing_user_email = Users.query.filter_by(email=email).first()
        existing_user_name = Users.query.filter_by(username=username).first()

        if existing_user_email or existing_user_name is not None:
            return UserStates.ALREADY_EXISTING

        new_user = Users(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return UserStates.CREATED

    def __create_registration_form(self):
        return RegisterForm(request.form)

    def __check_user_validity(self, register_form):
        if register_form.validate():
            state = self.__register_to_db(register_form=register_form)

            if state == UserStates.ALREADY_EXISTING:
                flash(
                    "User with such email or username already exists!", category="error"
                )
                return render_template(
                    "register.html",
                    register_form=self.__create_registration_form(),
                    user=current_user,
                )

            elif state == UserStates.CREATED:
                flash("User account successfully created!", category="success")
                return redirect(url_for("login"))
        else:
            flash("Form data is not valid!", category="error")

        return render_template(
            "register.html",
            register_form=self.__create_registration_form(),
            user=current_user,
        )

    def get(self):
        register_form = self.__create_registration_form()
        return render_template(
            "register.html", register_form=register_form, user=current_user
        )

    def post(self):
        register_form = self.__create_registration_form()
        return self.__check_user_validity(register_form=register_form)


class LoginView(MethodView):
    def __create_login_form(self):
        return LoginForm(request.form)

    def __find_user(self, username):
        return Users.query.filter_by(username=username).first()

    def __check_user_validity(self, login_form):
        if login_form.validate():
            username = request.form.get("username")
            password = request.form.get("password")

            user = self.__find_user(username)
            if user:
                if bcrypt.check_password_hash(user.password, password=password):
                    flash("Logged in successfully!", category="success")
                    login_user(user=user, remember=True)
                    return redirect(url_for("home"))
                else:
                    flash("Incorrect password, try again!", category="error")
            else:
                flash("Username does not exist!", category="error")

        return render_template("login.html", login_form=login_form, user=current_user)

    def get(self):
        login_form = self.__create_login_form()
        return render_template("login.html", login_form=login_form, user=current_user)

    def post(self):
        login_form = self.__create_login_form()
        return self.__check_user_validity(login_form=login_form)


class LogoutView(View):
    def dispatch_request(self):
        flash("Goodbye!")
        logout_user()
        return redirect(url_for("login"))


class ProfileView(MethodView):
    def dispatch_request(self):
        return render_template("profile.html", user=current_user)
