from flask import (current_app, flash, redirect, session,render_template, request, url_for)
from flask_login import current_user, login_required

from app import db
from app.models import User, Course, User_Course
from . import course_blueprint


@course_blueprint.route('/detail/<course_id>', methods=['GET', 'POST'])
@login_required
def detail(course_id):
    course_info = Course.query.filter_by(id=course_id).first()
    user_slides = User_Course.query.filter_by(course_id=course_id, user_id=current_user.id).first()
    if user_slides is not None:
        # wyliczenie procentu kursu użytkownika na podstawie
        print((course_info.last_slide - course_info.first_slide))
        print(user_slides.slideNumber)
        percent = ((int(user_slides.slideNumber)) / (int(course_info.last_slide) - int(course_info.first_slide))) * 100.0
        print(percent)
        return render_template('detail.html', course_info=course_info, course_percent=percent)
    return render_template('detail.html', course_info=course_info)



@course_blueprint.route('/course/<course_id>', methods=['GET', 'POST'])
@login_required
def course(course_id):
    session['course_id'] = course_id
    course_info = Course.query.filter_by(id=course_id).first()
    course_percent = User_Course.query.filter_by(course_id=course_id, user_id=current_user.id).first()
    if course_percent is None:
        course_percent = User_Course(course_id=course_id, user_id=current_user.id, percent=0)
        db.session.add(course_percent)
        db.session.commit()
    return render_template('course.html', course_info=course_info, course_percent=course_percent)
