from flask import Blueprint, render_template, redirect, url_for, request, flash
from webapp.models import Stump, City, Stump_type
from werkzeug.utils import secure_filename
import webapp.config as config
from . import db

import os

#create_stump = Blueprint('upload_image', __name__)
upload_image = Blueprint('upload_image', __name__)


def allowed_image(filename):

    if not '.' in filename:
        return False

    ext = filename.rsplit('.', 1)[1]

    if ext.upper() in config.ALLOWED_IMAGE_EXTENSIONS:
        return True
    else:
        return False


#@create_stump.route('/create_stump', methods=['GET', 'POST'])
#def create_stump_post():
@upload_image.route('/upload_image', methods=['GET', 'POST'])
def upload_file():
    ''' IMPORTANT this version is just for POC'''
    if request.method == 'POST':
 
        if request.files:
 
            image = request.files['image']
 
            if image.filename == '':
                print('No filename')
                return redirect(request.url)
 
            if allowed_image(image.filename):
                filename = secure_filename(image.filename)
                image.save(os.path.join(config.PATH_TO_UPLOAD_IMAGES, filename))
                print('Image saved')

                latitude = 49.215519
                #request.form.get('latitude')
                longitude = 16.579864
                #request.form.get('latitude')
                image_url = filename

                city_id = 1
                stump_type_id = 4 
                #db.Column(db.Integer, db.ForeignKey('stump_type.id'))
                
                new_stump = Stump(
                        latitude = latitude,
                        longitude = longitude,
                        image_url = image_url,
                        city_id = city_id,
                        stump_type_id = stump_type_id,
                        )

                db.session.add(new_stump)
                db.session.commit()

                return redirect(request.url)
            else:
                print('That file extension is not allowed')
                #todo return 405
                return redirect(request.url)

    return render_template('upload_image.html')
            
'''
#todo insert check for the City from the list of cities.
#    if not (City.query.filter_by(name=city_id).first())

#todo to add check for the correct stump type
#    if not (Stump_type.query.filter_by(name=stump_type_id).first())
'''

