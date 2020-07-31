#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from app.models import db, datetime, UserMixin
from .create_movie_user_table import movie_user


class User(db.Model, UserMixin):  # TODO(jsgonzlez661): Model users for api

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    encrypted_password = db.Column(db.String(94), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    movie_user = db.relationship(
        'Movie', secondary=movie_user, backref=db.backref('userMovie',
                                                          lazy='dynamic'))

    def verify_password(self, password):  # TODO(jsgonzlez661): Check password
        return check_password_hash(self.encrypted_password, password)

    @property
    def password(self):
        pass

    @password.setter
    def password(self, value):  # TODO(jsgonzlez661): Encrypt password
        self.encrypted_password = generate_password_hash(value)

    def __str__(self):
        return self.username

    @classmethod
    # TODO(jsgonzlez661): Save user in database
    def create_element(cls, username, email, password):
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod  # TODO(jsgonzlez661): Get user for username
    def get_by_username(cls, username):
        return User.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):  # TODO(jsgonzlez661): Get user for email
        return User.query.filter_by(email=email).first()

    @classmethod
    def get_by_id(cls, id):  # TODO(jsgonzlez661): Get user for id
        return User.query.filter_by(id=id).first()
