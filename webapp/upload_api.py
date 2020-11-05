from flask import Blueprint, render_template, request, redirect
from webapp.models import Stump, City, Stump_type
from werkzeug.utils import secure_filename
import webapp.config as config
import json                                                     
import os
from . import db
import time


upload_api = Blueprint('upload_api', __name__)                                   


def save_file(uploaded_file):
    filename = (
        time.strftime("%Y%m%d-%H%M%S") + '.' + \
        secure_filename(uploaded_file.filename).rsplit('.', 1)[1]
    )
    # These commands are commented, while problem with filename is not solved, but it works 
    uploaded_file.save(os.path.join(
                          config.PATH_TO_UPLOAD_IMAGES,
                          filename))
    return 'uploads/'+filename


def process_json(data, filename):        
    city_id_q = City.query.filter_by(
        name=data['city']
                ).first().id

    stump_type_id_q = Stump_type.query.filter_by(
        name=data['stump_type']
                ).first().id

    print(stump_type_id_q)

    new_stump = Stump(
                    latitude = data['latitude'],
                    longitude = data['longitude'],
                    image_url = filename,
                    city_id = city_id_q,
                    stump_type_id = stump_type_id_q,
                    )
    print(filename)
    # These commands are commented, while problem with filename is not solved, but it works    
    db.session.add(new_stump)
    db.session.commit()


@upload_api.route('/upload_api',methods=['POST'])            
def test_api():
    #todo first thing first - apikey authorization         
    print(json.load(request.files['apikey']))                                  
    filename = save_file(request.files['filename'])
    #todo put into try
    process_json(json.load(request.files['data']),filename)
    return 'success'

