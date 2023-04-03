from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

from app.config import Config


db = SQLAlchemy()
flask_app = Flask(__name__)

flask_app.config.from_object(Config)
flask_app.secret_key = Config.SECRET_KEY

migrate = Migrate()
bcrypt = Bcrypt(flask_app)

db.init_app(app=flask_app)
migrate.init_app(app=flask_app, db=db)

from .views import IndexView, RegisterView, LoginView

flask_app.add_url_rule('/', view_func=IndexView.as_view('index'), methods=["GET"])
flask_app.add_url_rule('/register', view_func=RegisterView.as_view('register'), methods=["GET", "POST"])
flask_app.add_url_rule('/login', view_func=LoginView.as_view('login'), methods=["GET", "POST"])