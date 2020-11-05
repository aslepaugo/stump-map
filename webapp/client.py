import json
import requests

stump_json = {
    'latitude': 49.211281,
    'longitude': 16.591147,
    'city': 'Brno',
    'stump_type': 'dead sapling',
        }

apikey = {'apikey': 'The Quick Brown Fox Jumped'}

filename = '/media/sf_projects/for_pirates/IMG_6914.JPG'

url = "http://localhost:5000/upload_api"

files = [
    ('filename', (filename, open(filename, 'rb'), 'application/octet')),
    ('data', ('data', json.dumps(stump_json), 'application/json')),
    ('apikey', ('apikey', json.dumps(apikey), 'application/json')),
]

r = requests.post(url, files=files)
print(r)