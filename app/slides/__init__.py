from flask import Blueprint

slides_blueprint = Blueprint('slides',
                            __name__,
                            template_folder='templates')

from . import routes
