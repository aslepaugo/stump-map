from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))


class Invite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invite_code = db.Column(db.String(20), unique=True)
    expire_date = db.Column(db.DateTime)


class Stump(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
