from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
import folium
from folium import plugins

from webapp.models import Stump, City, Stump_type
from webapp.config import DEFAULT_CITY, USER_AGENT
from geopy.geocoders import Nominatim

main = Blueprint('main', __name__)


@main.route('/')
def index():

    requested_city = request.args.get('city')
    if requested_city is None:
        requested_city = DEFAULT_CITY

    stumps = Stump.query.join(City).filter(City.name == requested_city).join(Stump_type).all()
    stumps_count = len(stumps)
    city_list = City.query.order_by(City.name).all()

    if stumps_count == 0:
        geolocator = Nominatim(user_agent=USER_AGENT)
        location = geolocator.geocode(requested_city)
        if location is None:
            flash("Unknown city {}!".format(requested_city))
            requested_city = DEFAULT_CITY
            location = geolocator.geocode(requested_city)
            stumps = Stump.query.join(City).filter(City.name == requested_city).join(Stump_type).all()
            stumps_count = len(stumps)

        base_latitude = location.latitude
        base_longitude = location.longitude
    else:
        base_latitude = stumps[0].latitude
        base_longitude = stumps[0].longitude

    map = folium.Map(
        location=[base_latitude, base_longitude],
        zoom_start=13,
        tiles='OpenStreetMap',
        scrollWheelZoom=False)

    marker_cluster = plugins.MarkerCluster().add_to(map)

    for stump in stumps:

        latitude = stump.latitude
        longitude = stump.longitude

        stump_description = "<a href='/details/{}' target='_PARENT'>{}</a> ".format(stump.id, stump.stump_type.name)

        stump_icon = folium.Icon(
                color=stump.stump_type.color,
                icon='envira',
                angle=180,
                prefix='fa')

        folium.Marker(
            [latitude, longitude],
            popup=stump_description,
            icon=stump_icon
            ).add_to(marker_cluster)

    return render_template(
        'index.html',
        map=map._repr_html_(),
        city_list=city_list,
        city=requested_city,
        stumps_count=stumps_count)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', email=current_user.email)
