#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.schemas import ma
from app.schemas.movie_schema import GenreGetMovieSchema


class GenreSchema(ma.Schema):

    genre = ma.Nested(GenreGetMovieSchema, many=True)

    class Meta:

        fields = ('id', 'genere_name', 'genre')


# TODO(jsgonzlez661): Get one genre
schema_genre = GenreSchema()
# TODO(jsgonzlez661): Get all genre
schemas_genre = GenreSchema(many=True)
