#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.models import db, datetime
from .create_movie_actor_table import movie_actor


class Actor(db.Model):  # TODO(jsgonzlez661): Model actor for database

    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(250),  nullable=False)
    lastname = db.Column(db.String(250),  nullable=False)
    nationality = db.Column(db.String(250),  nullable=False)
    movie_actors = db.relationship(
        'Movie', secondary=movie_actor, backref=db.backref('actorMovie',
                                                           lazy='dynamic'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    @classmethod
    def get_by_firstname(cls, firstname):
        return Actor.query.filter_by(firstname=firstname).first()

    @classmethod
    def get_by_lastname(cls, lastname):
        return Actor.query.filter_by(lastname=lastname).first()

    @classmethod
    def get_by_nationality(cls, lastname):
        return Actor.query.filter_by(lastname=lastname).first()
