from flask_login import UserMixin
from . import db
from sqlalchemy.orm import relationship
from datetime import datetime


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


class Stump_status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)


class Stump(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    image_url = db.Column(db.String)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())

    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    stump_type_id = db.Column(db.Integer, db.ForeignKey('stump_type.id'))
    stump_status_id = db.Column(db.Integer, db.ForeignKey('stump_status.id'))

    city = relationship("City")
    stump_type = relationship("Stump_type")
    stump_status = relationship("Stump_status")


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())

    stump_id = db.Column(
        db.Integer,
        db.ForeignKey('stump.id', ondelete='CASCADE'),
        index=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True
    )

    news = relationship('Stump', backref='comments')
    user = relationship('User', backref='comments')
