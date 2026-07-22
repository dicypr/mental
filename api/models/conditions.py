from enum import unique

from api import db


class Condition(db.Model):
    __tablename__ = "conditions"
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(80), unique=True, nullable=False)
    desc = db.Column(db.String(200))
    # resources = db.relationship("Resource", backref="condition", lazy="dynamic")
