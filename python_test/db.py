import sqlalchemy as sa
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import func


class Base(Model):
    created_at = sa.Column(sa.DateTime(timezone=True), default=func.now())
    updated_at = sa.Column(sa.DateTime(timezone=True), default=func.now(), onupdate=func.now())


db = SQLAlchemy(session_options={"autoflush": False, "autocommit": False}, model_class=Base)
