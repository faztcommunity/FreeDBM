#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.models import db

# TODO(jsgonzlez661): Table pivote movie - actor
movie_actor = db.Table('movie_actor',
                       db.Column('movie_id', db.Integer, db.ForeignKey(
                           'movies.id'), primary_key=True),
                       db.Column('actor_id', db.Integer, db.ForeignKey(
                           'actors.id'), primary_key=True),
                       )
