from datetime import datetime
import numpy as np
from uuid import uuid4
import os

from colander import Schema
from werkzeug.security import generate_password_hash, check_password_hash
from websauna.system.model.columns import UUID

from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(80), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    uuid = db.Column(UUID(as_uuid=True), default=uuid4)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.registered_on = datetime.utcnow()
    def compare_password(self, password):
        return check_password_hash(self.password_hash, password)
    def new_password(self, password):
        self.password_hash = generate_password_hash(password)
    def __repr__(self):
        return f'<User: {self.email}>'
    @property
    def is_authenticated(self):
        return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)
    def get_uuid(self):
        return str(self.uuid)


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    first_slide = db.Column(db.Integer, nullable=False)
    last_slide = db.Column(db.Integer, nullable=False)

    def __init__(self, name, description, first_slide, last_slide):
        self.name = name
        self.description = description
        self.first_slide = first_slide
        self.last_slide = last_slide
    def __repr__(self):
        return f'<Course: {self.name}>'

class User_Course(db.Model):
    __tablename__ = 'user_courses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    slideNumber = db.Column(db.Integer, nullable=False)

    #kursy wpisane do usera
    user = db.relationship('User', backref=db.backref('user_courses', cascade='all, delete-orphan'))
    #userzy wpisani do kursów
    course = db.relationship('Course', backref=db.backref('user_courses', cascade='all, delete-orphan'))

    def __init__(self, user_id, course_id):
        self.user_id = user_id
        self.course_id = course_id
        self.slideNumber = 0
    def __repr__(self):
        return f'<UserCourse: User {self.user_id} enrolled in Course {self.course_id}>'





"""
class Chapters(db.Model):
    __tablename__ = 'chapters'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)

    def __init__(self, name, description, course_id, number):
        self.name = name
        self.description = description
        self.course_id = course_id
        self.number = number
    def __repr__(self):
        return f'<Chapter: {self.name}>'


class Slides(db.Model):
    __tablename__ = 'slides'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(1000), unique=True, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=False)

    def __init__(self, content, course_id):
        self.content = content
        self.course_id = course_id
    def __repr__(self):
        return f'<Slide: {self.content}>'
"""
