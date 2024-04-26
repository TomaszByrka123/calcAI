from flask import (current_app, flash, redirect, render_template, request, url_for)
from flask_login import current_user, login_required, login_user, logout_user

from app import db
from app.models import User, Course, User_Course
from . import course_blueprint


@course_blueprint.route('/detail/<course_name>', methods=['GET', 'POST'])
@login_required
def detail(course_name):
    course_info = User_Course.query.filter_by(user_id=current_user.id).all()

    course_name = User_Course.execute("SELECT * FROM kursy WHERE nazwa=?", (course_name,))
    course_detail = Course.query.filter_by(name=course_name).first()

    return render_template('detail.html', course_detail=course_detail, course_name=course_name)