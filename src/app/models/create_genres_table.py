#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.models import db, datetime
from .create_movie_genre_table import movie_geners


class Gener(db.Model):  # TODO(jsgonzlez661): Model geners for database

    __tablename__ = 'geners'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genere_name = db.Column(db.String(250),  nullable=False)
    genre = db.relationship('Movie', secondary=movie_geners,
                            backref=db.backref('genreMovie', lazy='dynamic'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    @classmethod
    def get_by_genere_name(cls, genere_name):
        return Gener.query.filter_by(genere_name=genere_name).first()
