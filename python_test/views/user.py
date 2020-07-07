import flask as fl
from flask import Blueprint

from python_test.db import db
from python_test.models.user import User

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/login", methods=["GET"])
def login_page():
    return fl.render_template("login.jinja2")


@bp.route("/login", methods=["POST"])
def login():
    frm = fl.request.form

    user = db.session.query(User).filter_by(user_id=frm.get("user_id")).first()
    if not user:
        return fl.jsonify({"ok": False, "title": "User Not Found"})

    if user.user_pw != frm.get("user_pw"):
        return fl.jsonify({"ok": False, "title": "Wrong Password"})

    return fl.jsonify({"ok": True, "title": f"Welcome {user.name}!"})
