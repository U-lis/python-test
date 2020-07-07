from flask import Flask

from python_test.db import db

app = Flask(__name__, static_folder="python_test/static", template_folder="python_test/templates")

db.init_app(app)


@app.route("/ping")
def ping():
    return "pong"