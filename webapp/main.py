from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
import folium

main = Blueprint('main', __name__)


@main.route('/')
def index(city="Brno", stump_type="Stump"):

    stumps = Stump.query.all()

    map = folium.Map(
        location=[49.211169, 16.592006],
        zoom_start=13,
        tiles='OpenStreetMap',
        scrollWheelZoom=False)

    folium.Marker([49.211169, 16.590006]).add_to(map)

    for stump in stumps:

        latitude = stump.lattitude
        longitude = stump.longitude

        stump_description = "Click <a href='/details/{}' target='_PARENT'>here</a> to get more details".format(stump.id)

        stump_icon = folium.Icon(
                color='darkred',
                icon='envira',
                angle=180,
                prefix='fa')

        folium.Marker(
            [latitude, longitude],
            popup=stump_description,
            icon=stump_icon
            ).add_to(map)

    return render_template('index.html', map=map._repr_html_())


@main.route('/search', methods=['POST'])
def search():

    city = request.form.get('city')
    stump_type = request.form.get('type')

    print(city, " ", stump_type)

    # geolocator = Nominatim(user_agent="stump-map")
    # location = geolocator.geocode(request.form.get('search'))
    # print((location.latitude, location.longitude), file=sys.stdout)

    return redirect(url_for('main.index'))


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', email=current_user.email)
