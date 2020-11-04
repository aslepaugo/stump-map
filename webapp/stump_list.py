from flask import Blueprint, render_template
from webapp.models import Stump, City, Stump_type

stumps = Blueprint('stumps', __name__)


@stumps.route('/stumps', methods=['GET'])
def stumps_list():
    stumps = Stump.query.join(City).join(Stump_type)

    return render_template('stumps.html',
                           stumps=stumps,
                           )
