from flask import Blueprint

course_blueprint = Blueprint('course',
                            __name__,
                            template_folder='templates')

from . import routes
