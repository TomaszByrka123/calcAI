from flask import Blueprint

course_blueprint = Blueprint('courses',
                            __name__,
                            template_folder='templates')

from . import routes
