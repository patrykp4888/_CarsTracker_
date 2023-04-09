from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from app.config import Config


db = SQLAlchemy()
flask_app = Flask(__name__)

flask_app.config.from_object(Config)
flask_app.secret_key = Config.SECRET_KEY

migrate = Migrate()
bcrypt = Bcrypt(flask_app)

db.init_app(app=flask_app)
migrate.init_app(app=flask_app, db=db)

from .views import IndexView, RegisterView, LoginView, LogoutView, HomeView, ProfileView

flask_app.add_url_rule("/", view_func=IndexView.as_view("index"), methods=["GET"])
flask_app.add_url_rule(
    "/home", view_func=HomeView.as_view("home"), methods=["GET", "POST"]
)
flask_app.add_url_rule(
    "/register", view_func=RegisterView.as_view("register"), methods=["GET", "POST"]
)
flask_app.add_url_rule(
    "/login", view_func=LoginView.as_view("login"), methods=["GET", "POST"]
)
flask_app.add_url_rule(
    "/logout", view_func=LogoutView.as_view("logout"), methods=["GET"]
)
flask_app.add_url_rule(
    "/profile", view_func=ProfileView.as_view("profile"), methods=["GET", "POST"]
)

from .models.users import Users

login_manager = LoginManager()
login_manager.login_view = "views.login"
login_manager.init_app(flask_app)


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
