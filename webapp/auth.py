from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Invite, City
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login():
    city_list = City.query.order_by(City.name).all()
    return render_template('login.html', city_list=city_list)


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user)
    return redirect(url_for('main.profile'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/signup', methods=['GET'])
def signup():
    city_list = City.query.order_by(City.name).all()
    return render_template('signup.html', city_list=city_list)


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')
    verified_password = request.form.get('verified_password')
    invite_code = request.form.get('invite_code')

    if password != verified_password:
        flash('Passwords are not simillar')
        return redirect(url_for('auth.signup'))

    invite = Invite.query.filter_by(invite_code=invite_code).first()

    if not invite:
        flash('Wrong or expired invite code')
        return redirect(url_for('auth.signup'))

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email,
                    password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))
