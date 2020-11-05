SECRET_KEY = 'secret-key-goes-here'
SQLALCHEMY_TRACK_MODIFICATIONS = True
TEMPLATES_AUTO_RELOAD = True
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost:5430/stump_map'

DEFAULT_CITY = 'Brno'
USER_AGENT = 'stump-application'
STUMPS_PER_PAGE = 10

PATH_TO_UPLOAD_IMAGES='/media/sf_projects/pet_project/stump-map/webapp/static/uploads/'
ALLOWED_IMAGE_EXTENSIONS='JPEG', 'JPG', 'PNG', 'GIF'
API_KEY='very_long_bs'