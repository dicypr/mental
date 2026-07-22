from datetime import datetime

from api import db


class Goals(db.Model):
    __tablename__ = "goals"
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(
    #    db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    # )
    goal_name = db.Column(db.String(80), nullable=False)
    goal_description = db.Column(db.String(200), nullable=False)
    target = db.Column(db.DateTime, default=datetime.now)
    goal_points = db.Column(db.Integer, nullable=False)

    # user = db.relationship("User", secondary="user_name", backref="goals")
