from datetime import datetime
import numpy as np
from uuid import uuid4
import os

from colander import Schema
from werkzeug.security import generate_password_hash, check_password_hash
from websauna.system.model.columns import UUID

from app import db
from main import app

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
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return f'<Course: {self.name}>'

class User_Course(db.Model):
    __tablename__ = 'user_courses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    percent = db.Column(db.Float, nullable=False)

    #kursy wpisane do usera
    user = db.relationship('User', backref=db.backref('user_courses', cascade='all, delete-orphan'))
    #userzy wpisani do kursów
    course = db.relationship('Course', backref=db.backref('user_courses', cascade='all, delete-orphan'))

    def __init__(self, user_id, course_id, percent):
        self.user_id = user_id
        self.course_id = course_id
        self.percent = 0
    def __repr__(self):
        return f'<UserCourse: User {self.user_id} enrolled in Course {self.course_id}>'


class Chapters(db.Model):
    __tablename__ = 'chapters'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)

    def __init__(self, name, course_id, number):
        self.name = name
        self.course_id = course_id
        self.number = number
    def __repr__(self):
        return f'<Chapter: {self.name}>'


class Images(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    path = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def url(self):
        # Assuming the images are stored in a folder called 'images' in the static directory
        return os.path.join(app.static_url_path, 'images', self.path)

    def __repr__(self):
        return f'<Image: {self.name}>'

class Slides(db.Model):
    __tablename__ = 'slides'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(1000), unique=True, nullable=False)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=False)
    image = db.Column(db.Integer, db.ForeignKey('images.id'), nullable=True)

    def __init__(self, content, chapter_id, image):
        self.content = content
        self.chapter_id = chapter_id
        self.image = image
    def __repr__(self):
        return f'<Slide: {self.content}>'
