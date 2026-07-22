from datetime import datetime
from operator import index

from api import db


class Appointments(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)
    # customer_id = db.Column(
    #    db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    # )
    timeslot = db.Column(db.DateTime, default=datetime.now)
    problem = db.Column(db.String(100))

    # customer = db.relationship(
    #    "User", secondary="user_customer", backref="appointments"
    # )
