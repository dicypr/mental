from api import db


class Resource(db.Model):
    __tablename__ = "resource"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    link = db.Column(db.String(200), unique=True, nullable=False)
    # condition_id = db.Column(db.Integer, db.ForeignKey('condition.id', ondelete='CASCADE'), nullable=False)
    # condition = db.relationship('Condition', backref='resources')
