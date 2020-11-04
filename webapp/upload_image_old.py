from flask import Blueprint, render_template, request, redirect
from webapp.models import Stump, City, Stump_type
from werkzeug.utils import secure_filename
import webapp.config as config

import os

upload_image = Blueprint('upload_image', __name__)


def allowed_image(filename):

    if not '.' in filename:
        return False

    ext = filename.rsplit('.', 1)[1]

    if ext.upper() in config.ALLOWED_IMAGE_EXTENSIONS:
        return True
    else:
        return False

        
@upload_image.route('/upload_image', methods=['GET', 'POST'])
def upload_file():
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
                return redirect(request.url)
            else:
                print('That file extension is not allowed')
                #todo return 405
                return redirect(request.url)

    return render_template('upload_image.html')