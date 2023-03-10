from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Define schema
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char_name = db.Column(db.String(50))
    char_race = db.Column(db.String(50))
    char_class = db.Column(db.String(50))
    char_background = db.Column(db.String(50))
    char_alignment = db.Column(db.String(50))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    characters = db.relationship('Character')