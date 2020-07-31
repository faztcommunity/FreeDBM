#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.models import db, datetime
from .create_movie_director_table import movie_director


class Director(db.Model):  # TODO(jsgonzlez661): Model director for database

    __tablename__ = 'director'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(250),  nullable=False)
    lastname = db.Column(db.String(250),  nullable=False)
    movie_director = db.relationship(
        'Movie', secondary=movie_director, backref=db.backref('directorMovie',
                                                              lazy='dynamic'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    @classmethod
    def get_by_firstname(cls, firstname):
        return Director.query.filter_by(firstname=firstname).first()

    @classmethod
    def get_by_lastname(cls, lastname):
        return Director.query.filter_by(lastname=lastname).first()
