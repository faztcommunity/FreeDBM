#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.models import db

# TODO(jsgonzlez661): Table pivote movie - user
movie_user = db.Table('movie_user',
                      db.Column('user_id', db.Integer, db.ForeignKey(
                          'users.id'), primary_key=True),
                      db.Column('movie_id', db.Integer, db.ForeignKey(
                          'movies.id'), primary_key=True),
                      )
