from flask import render_template, url_for, redirect, flash, request
from flask.views import View, MethodView
from flask_login import login_user, logout_user, login_required, current_user

from app import db, bcrypt
from .states import UserStates
from .models import Users
from .forms import RegisterForm, LoginForm


class IndexView(View):

    def dispatch_request(self):
        if request.method == "GET":
            return render_template("base.html", user=current_user)
        elif request.method == "POST":
            return render_template("base.html", user=current_user)
    

class HomeView(View):

    def dispatch_request(self):
        if request.method == "GET":
            return render_template("home.html", user=current_user)
        elif request.method == "POST":
            return render_template("home.html", user=current_user)


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
        return  RegisterForm(request.form)
    
    def __check_user_validity(self, register_form):
        if register_form.validate():

            state = self.__register_to_db(register_form=register_form)

            if state == UserStates.ALREADY_EXISTING:
                flash("User with such email or username already exists!", category='error')
                return render_template('register.html', register_form=RegisterForm(), user=current_user)
            
            elif state == UserStates.CREATED:
                flash("User account successfully created!", category='success')
                return redirect(url_for('login'), user=current_user)
        else:
            flash('Form data is not valid!', category='error')

        return render_template('register.html', register_form=RegisterForm(), user=current_user)


    def get(self):
        register_form = self.__create_registration_form()
        return render_template("register.html", register_form=register_form, user=current_user)

    def post(self):
        register_form = self.__create_registration_form()
        return self.__check_user_validity(register_form=register_form)  


class LoginView(MethodView):

    def get(self):
        login_form = LoginForm(request.form)
        return render_template("login.html", login_form=login_form, user=current_user)

    def post(self):
        login_form = LoginForm(request.form)
        if login_form.validate():
            username = request.form.get('username')
            password = request.form.get('password')

            user = Users.query.filter_by(username=username).first()
            if user:
                if bcrypt.check_password_hash(user.password, password=password):
                    flash('Logged in successfully!', category='success')
                    login_user(user=user, remember=True)
                    return redirect(url_for('home'))
                else:
                    flash('Incorrect password, try again!', category='error')
            else:
                flash('Email does not exist!', category='error')

        return render_template('login.html', login_form=login_form, user=current_user)


class LogoutView(View):

    def dispatch_request(self):
        flash('Goodbye!')
        logout_user()
        return redirect(url_for('login'))