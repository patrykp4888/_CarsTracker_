from flask import Flask

from app.views import IndexView


flask_app = Flask(__name__)


flask_app.add_url_rule('/', view_func=IndexView.as_view('index'))