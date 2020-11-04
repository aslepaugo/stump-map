from flask import Blueprint, render_template, url_for
from webapp.models import Stump, City, Stump_type
from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired
from webapp.models import Comment
from webapp import db
from flask import flash, redirect, request
from flask_login import current_user

stump_details = Blueprint('stump', __name__)


@stump_details.route('/stumps/details/<int:id>')
def stump_detail(id):

    city_list = City.query.order_by(City.name).all()

    stump = Stump.query.get(id)
    form = CommentForm(stump_id=stump.id)

    if stump.image_url is None:
        stump.image_url = 'img/default.jpg'
    image_url = url_for('static', filename=stump.image_url)
    return render_template('stump.html', stump=stump, image_url=image_url, city_list=city_list, comment_form=form)


@stump_details.route('/stump/comment', methods=['POST'])
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        if Stump.query.filter(Stump.id == form.stump_id.data).first():
            comment = Comment(text=form.comment_text.data, stump_id=form.stump_id.data, user_id=current_user.id)
            db.session.add(comment)
            db.session.commit()
            flash('Comment has been added')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Error in field "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
    return redirect(request.referrer)

class CommentForm(FlaskForm):
    stump_id = HiddenField('StumpID', validators=[DataRequired()])
    comment_text = StringField('Comment', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Post', render_kw={"class": "btn btn-primary"})
