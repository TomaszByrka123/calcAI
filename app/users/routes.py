import sqlalchemy as sa
from flask import (current_app, flash, redirect, render_template, request,
                   url_for)
from flask_login import current_user, login_required, login_user, logout_user


from app import db
from app.models import User, User_Course
from . import users_blueprint
from .forms import LoginForm, RegisterForm

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.profile'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.compare_password(form.password.data):
            db.session.add(user)
            db.session.commit()
            login_user(user, form.remember_me.data)
            return redirect(url_for('users.mainPage'))
        else:
            flash("Invalid username or password")
            return redirect(url_for('users.login'))

    return render_template('login.html', form=form)

@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if not current_app.config['BLOKADA_REJESTRACJI']:
        return redirect(url_for('users.login'))

    if current_user.is_authenticated:
        return redirect(url_for('users.profile'))

    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit() and form.statute.data:
        new_user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()

        user_course = User_Course(new_user.get_id())
        db.session.add(user_course)
        db.session.commit()


        login_user(new_user)
        return redirect(url_for('users.profile'))
    return render_template('register.html', form=form)

@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))

@users_blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@users_blueprint.route('/mainPage', methods=['GET', 'POST'])
@login_required
def mainPage():
    return render_template('mainPage.html', user=current_user)