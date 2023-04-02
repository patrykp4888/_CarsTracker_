from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

from app.views import IndexView
from app.config import Config


db = SQLAlchemy()
flask_app = Flask(__name__)

flask_app.config.from_object(Config)
flask_app.secret_key = Config.SECRET_KEY

migrate = Migrate(flask_app, db)
bcrypt = Bcrypt(flask_app)

db.init_app(app=flask_app)
migrate.init_app(app=flask_app, db=db)


flask_app.add_url_rule('/', view_func=IndexView.as_view('index'))