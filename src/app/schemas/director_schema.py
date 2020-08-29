#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.schemas import ma
from app.schemas.movie_schema import DirectorGetMovieSchema


class DirectorSchema(ma.Schema):

    movie_director = ma.Nested(DirectorGetMovieSchema, many=True)

    class Meta:
        fields = ('id', 'fullname', 'movie_director')


# TODO(jsgonzlez661): Get one info director
schema_director = DirectorSchema()
# TODO(jsgonzlez661): Get all info directors
schemas_director = DirectorSchema(many=True)
