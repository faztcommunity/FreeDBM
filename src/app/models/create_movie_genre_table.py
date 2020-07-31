#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.models import db

# TODO(jsgonzlez661): Table pivote movie - genre
movie_geners = db.Table('movie_geners',
                        db.Column('movie_id', db.Integer, db.ForeignKey(
                            'movies.id'), primary_key=True),
                        db.Column('genre_id', db.Integer, db.ForeignKey(
                            'geners.id'), primary_key=True),
                        )
