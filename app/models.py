from datetime import datetime
import numpy as np
from uuid import uuid4

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

class User_Course(db.Model):
    __tablename__ = 'user_courses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    course_name = db.Column(db.String, nullable=False)
    course_count = db.Column(db.Integer, default=0)
