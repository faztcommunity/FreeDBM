#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.models import db

# TODO(jsgonzlez661): Table pivote movie - director
movie_director = db.Table('movie_director',
                          db.Column('movie_id', db.Integer, db.ForeignKey(
                              'movies.id'), primary_key=True),
                          db.Column('director_id', db.Integer, db.ForeignKey(
                              'director.id'), primary_key=True),
                          )
