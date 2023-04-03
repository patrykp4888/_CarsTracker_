from flask import render_template, url_for, redirect, flash, request
from flask.views import View, MethodView

from app import db
from .states import UserStates
from .models import Users
from .forms import RegisterForm


class IndexView(View):
    def __init__(self):
        self.welcome_text = "Hello!"

    def dispatch_request(self):
        return render_template("index.html")
    

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

    def get(self):
        register_form = RegisterForm(request.method)
        return render_template("register.html", register_form=register_form)

    def post(self):
        register_form = RegisterForm(request.method)
        if register_form.validate():
            state = self.__register_to_db(register_form=register_form)

            if state == UserStates.ALREADY_EXISTING:
                flash("User with such email or username already exists!")
                return render_template('register.html', register_form=RegisterForm())
            elif state == UserStates.CREATED:
                flash("User account successfully created!")
                redirect(url_for('login'))

        flash('Form data is not valid!')
        return render_template('register.html', register_form=RegisterForm())    


class LoginView(MethodView):

    def __login_user(self):
        ...