import json
import requests

stump_json = {
    'latitude': 49.215769,
    'longitude': 16.580964,
    'city': 'Brno',
    'stump_type': 'dead sapling',
        }

filename = '/media/sf_projects/for_pirates/IMG_6883.JPG'

url = "http://localhost:5000/upload_api"

files = [
    ('filename', (filename, open(filename, 'rb'), 'application/octet')),
    ('data', ('data', json.dumps(stump_json), 'application/json')),
]

r = requests.post(url, files=files)
print(r)