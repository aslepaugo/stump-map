import os
import logging
import json
import requests
from io import BytesIO
import settings



def save_coordinates(coordinates, context):
    context.user_data['longitude'] = float(coordinates['longitude'])
    # print(float(coordinates['longitude']))
    context.user_data['latitude'] = float(coordinates['latitude'])
    logging.info(str(context.user_data['longitude']))
    logging.info(str(context.user_data['latitude']))


def save_photo(update, context):
    update.message.reply_text("Saving photo")
    os.makedirs('downloads', exist_ok=True)
    photo_file = context.bot.getFile(update.message.photo[-1].file_id)
    filename = os.path.join('downloads', f'{photo_file.file_id}.jpg')
    photo_file.download(filename)
    context.user_data['file'] = filename
    update.message.reply_text("File saved")


def send_photo(update, context):
    context.user_data['file'] = context.bot.getFile(update.message.photo[-1].file_id)


def save_category(category, context):
    context.user_data['category'] = category
    logging.info('final check, what do we have in context.user_data')
    logging.info('Longitude ' + str(context.user_data['longitude']))
    logging.info('Latitude ' + str(context.user_data['latitude']))
    logging.info('button category ' + str(context.user_data['category']))
    # print(context.user_data['file'])
    # logging.info('photo' )
    

def send_request(context):
    stump_json = {
        'latitude': context.user_data['latitude'],
        'longitude': context.user_data['longitude'],
        'city': 'Brno',
        'stump_type': context.user_data['category'],
        }

    apikey = {'apikey': settings.STUMPPAGE_API_KEY}

    file = context.user_data['file']
    filename = file.file_id+'.jpg' #todo fileextenstion extraction
    file_in_memory =  BytesIO(file.download_as_bytearray())
    file_in_memory.seek(0) # Return to beginning of buffer
    
    files = [
        # ('filename', (filename, open(filename, 'rb'), 'application/octet')),
        ('filename', (filename, file_in_memory.getvalue(), 'application/octet')),
        ('data', ('data', json.dumps(stump_json), 'application/json')),
        ('apikey', ('apikey', json.dumps(apikey), 'application/json')),
    ]

    r = requests.post(settings.STUMPPAGE_URL, files=files)
    print(r)

