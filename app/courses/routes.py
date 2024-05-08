from flask import (current_app, flash, redirect, render_template, request, url_for)
from flask_login import current_user, login_required, login_user, logout_user

from app import db
from app.models import User, Course, User_Course
from . import course_blueprint


@course_blueprint.route('/detail/<course_id>', methods=['GET', 'POST'])
@login_required
def detail(course_id):
    course_info = Course.query.filter_by(id=course_id).first()
    course_percent = User_Course.query.filter_by(course_id=course_id, user_id=current_user.id).first()
    if course_percent is None:
        return render_template('detail.html', course_info=course_info)
    return render_template('detail.html', course_info=course_info, course_percent=course_percent)


@course_blueprint.route('/course/<course_id>', methods=['GET', 'POST'])
@login_required
def course(course_id):
    course_info = Course.query.filter_by(id=course_id).first()
    course_percent = User_Course.query.filter_by(course_id=course_id, user_id=current_user.id).first()
    if course_percent is None:
        course_percent = User_Course(course_id=course_id, user_id=current_user.id, percent=0)
        db.session.add(course_percent)
        db.session.commit()
    return render_template('course.html', course_info=course_info, course_percent=course_percent)

