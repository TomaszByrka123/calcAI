from flask import (current_app, flash, redirect, session,render_template, request, url_for, jsonify)
from flask_login import current_user, login_required
from sqlalchemy import and_

from app import db
from app.models import User, Course, User_Course, Lessons
from . import course_blueprint


@course_blueprint.route('/detail/<course_id>', methods=['GET', 'POST'])
@login_required
def detail(course_id):
    session['course_id'] = course_id
    course_info = Course.query.filter_by(id=course_id).first()
    user_course_info = User_Course.query.filter_by(course_id=course_id, user_id=current_user.id).first()
    lesson_info = Lessons.query.filter_by(course_id=course_id).all()
    all_slides_in_course = lesson_info[len(lesson_info)-1].last_slide - lesson_info[0].first_slide + 1
    if user_course_info is not None:
        percent = round(((int(user_course_info.slideNumber)) / (all_slides_in_course)) * 100.0)
        return render_template('detail.html', course_info=course_info, lesson_info=lesson_info, course_percent=percent)
    return render_template('detail.html', course_info=course_info, lesson_info=lesson_info)



@course_blueprint.route('/course/<int:course_id>/<int:lesson_id>', methods=['GET', 'POST'])
@login_required
def course(course_id, lesson_id):
    session['course_id'] = course_id
    session['lesson_id'] = lesson_id
    course_info = Course.query.filter_by(id=course_id).first()
    user_course_info = User_Course.query.filter_by(course_id=course_id, user_id=current_user.id).first()
    if user_course_info is None:
        new_user_course = User_Course(course_id=course_id, user_id=current_user.id)
        db.session.add(new_user_course)
        db.session.commit()
    return render_template('course.html', course_info=course_info)


@course_blueprint.route('/continue_lesson', methods=['GET', 'POST'])
@login_required
def continue_lesson():
    user_course_info = User_Course.query.filter_by(course_id=session['course_id'], user_id=current_user.id).first()
    lesson_info = Lessons.query.filter(
        and_(
            Lessons.course_id == session['course_id'],
            Lessons.first_slide <= user_course_info.slideNumber,
            Lessons.last_slide >= user_course_info.slideNumber
        )
    ).first()
    return redirect(url_for('courses.course', course_id=session['course_id'], lesson_id=lesson_info.id))


@course_blueprint.route('/lessons/<lesson_id>', methods=['GET', 'POST'])
@login_required
def lessons(lesson_id):
    user_course_info = User_Course.query.filter_by(course_id=session['course_id'], user_id=current_user.id).first()
    actual_lesson = Lessons.query.filter(
        and_(
            Lessons.course_id == session['course_id'],
            Lessons.first_slide <= user_course_info.slideNumber,
            Lessons.last_slide >= user_course_info.slideNumber
        )
    ).first()
    if str(actual_lesson.id) >= str(lesson_id):
        return redirect(url_for('courses.course', course_id=session['course_id'], lesson_id=lesson_id))
    return jsonify(result='not')
