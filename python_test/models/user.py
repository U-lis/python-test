from python_test.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Text, nullable=False, unique=True)
    user_pw = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
