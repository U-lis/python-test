import flask as fl
from flask import Flask

from python_test.db import db
from python_test import views

app = Flask(__name__, static_folder="python_test/static", template_folder="python_test/templates")

db.init_app(app)

for view in views.__all__:
    app.register_blueprint(view.bp)


@app.route("/ping")
def ping():
    return "pong"


@app.route("/")
def index():
    return fl.render_template("index.jinja2")
