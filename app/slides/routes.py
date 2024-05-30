from flask import (current_app, flash, redirect, render_template, request, url_for, jsonify, session)
from flask_login import current_user, login_required

from app import db
from app.models import User, Course, User_Course, Lessons
from . import slides_blueprint

@slides_blueprint.route('/slide', methods=['GET', 'POST'])
@login_required
def slide():
    course_id = session['course_id']
    lesson_id = session['lesson_id']

    course_info = Course.query.filter_by(id=course_id).first()
    user_course_info = User_Course.query.filter_by(course_id=course_id, user_id=current_user.id).first()
    lesson_info = Lessons.query.filter_by(id=lesson_id).first()

    first_slide = lesson_info.first_slide
    user_slide_number = user_course_info.slideNumber

    if user_slide_number > lesson_info.last_slide:
        rendered_html = render_template('end.html')
        return jsonify(result=rendered_html)
    else:
        file_name = str(int(course_id) - 1) + '/' + str(user_slide_number) + '.html'
        rendered_html = render_template(file_name)
        user_course_info.slideNumber += 1
        db.session.commit()
        return jsonify(result=rendered_html)


@slides_blueprint.route('/all_slides', methods=['GET', 'POST'])
@login_required
def all_slides():
    course_id = session['course_id']
    lesson_id = session['lesson_id']

    course_info = Course.query.filter_by(id=course_id).first()
    user_course_info = User_Course.query.filter_by(course_id=course_id, user_id=current_user.id).first()
    lesson_info = Lessons.query.filter_by(id=lesson_id).first()

    actual_slide = user_course_info.slideNumber
    print(actual_slide)
    first_slide = lesson_info.first_slide

    html_content = ""
    for i in range(first_slide, actual_slide):
        file_name = str(int(course_id) - 1) + '/' + str(i) + '.html'
        print(file_name)
        rendered_html = render_template(file_name)
        html_content += rendered_html
    if int(actual_slide) >= int(lesson_info.last_slide) + 1:
        rendered_html = render_template('end.html')
        html_content += rendered_html
    return jsonify(result=html_content)
