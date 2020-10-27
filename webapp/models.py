from flask_login import UserMixin
from . import db
from sqlalchemy.orm import relationship


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))


class Invite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invite_code = db.Column(db.String(20), unique=True)
    expire_date = db.Column(db.DateTime)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)


class Stump_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    color = db.Column(db.String)


class Stump(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    image_url = db.Column(db.String)

    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    stump_type_id = db.Column(db.Integer, db.ForeignKey('stump_type.id'))

    city = relationship("City")
    stump_type = relationship("Stump_type")
