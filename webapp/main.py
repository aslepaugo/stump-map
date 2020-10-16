from flask import Blueprint, render_template
from flask_login import login_required, current_user
import folium

main = Blueprint('main', __name__)


@main.route('/')
def index():

    map = folium.Map(
        location=[49.211169, 16.592006],
        zoom_start=10,
        tiles='OpenStreetMap')

    folium.Marker([49.211169, 16.590006]).add_to(map)
    folium.Marker(
        [49.211109, 16.592056], icon=folium.Icon(icon='cloud')
        ).add_to(map)

    return render_template('index.html', map=map._repr_html_())


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', email=current_user.email)
