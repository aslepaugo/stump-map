from flask import Blueprint, render_template
from flask_paginate import Pagination, get_page_parameter, request
from webapp.models import Stump, City, Stump_type
import webapp.config as config

stumps = Blueprint('stumps', __name__)


@stumps.route('/stumps', methods=['GET'])
def stumps_list():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    stumps = Stump.query.join(City).join(Stump_type).paginate(page, config.STUMPS_PER_PAGE, False).items

    pagination = Pagination(
                    page=page,
                    total=Stump.query.count(),
                    search=False,
                    record_name='stumps',
                    css_framework='bootstrap4',
                    per_page=config.STUMPS_PER_PAGE)

    return render_template('stumps.html',
                           stumps=stumps,
                           pagination=pagination
                           )
