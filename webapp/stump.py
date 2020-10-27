from flask import Blueprint, render_template, url_for
from webapp.models import Stump, City, Stump_type

stump_details = Blueprint('stump', __name__)


@stump_details.route('/stumps/details/<int:id>')
def stump_detail(id):
    stump = Stump.query.get(id)
    if stump.image_url is None:
        stump.image_url = 'img/default.jpg'
    image_url = url_for('static', filename=stump.image_url)
    return render_template('stump.html', stump=stump, image_url=image_url)
