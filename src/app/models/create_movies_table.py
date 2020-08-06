#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.models import db
from .create_movie_user_table import movie_user
from .create_movie_genre_table import movie_geners
from .create_movie_actor_table import movie_actor
from .create_movie_director_table import movie_director


class Movie(db.Model):  # TODO(jsgonzlez661): Model movie for database

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250),  nullable=False)
    year = db.Column(db.String(250),  nullable=False)
    runtime = db.Column(db.String(250),  nullable=False)
    genre = db.relationship('Gener', secondary=movie_geners,
                            backref=db.backref('genreMovie', lazy='dynamic'))
    director = db.relationship('Director', secondary=movie_director,
                               backref=db.backref('directorMovie',
                                                  lazy='dynamic'))
    actor = db.relationship('Actor', secondary=movie_actor,
                            backref=db.backref('actorMovie', lazy='dynamic'))
    poster = db.Column(db.String(250),  nullable=False)
    synopsis = db.Column(db.Text(4294000000), nullable=False)
    user_id = db.relationship(
        'User', secondary=movie_user, backref=db.backref('userMovie',
                                                         lazy='dynamic'))
    imdb_rating = db.Column(db.String(50),  nullable=False)
