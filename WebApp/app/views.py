from flask import render_template
from flask.views import View, MethodView


class IndexView(View):
    def __init__(self):
        self.welcome_text = "Hello!"

    def dispatch_request(self):
        return render_template("index.html")