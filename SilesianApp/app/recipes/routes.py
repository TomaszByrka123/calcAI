from flask import render_template, send_from_directory, current_app
from . import recipes_blueprint

@recipes_blueprint.route('/')
def index():
    return render_template('index.html')

#to cos do maskowania drzewa plików dla osoby która będzie coś pobierać ze strony
@recipes_blueprint.route('/file/<path:filename>')
def download_file(filename):
    return send_from_directory(current_app.config['UPLOAD_PATH'], filename)

