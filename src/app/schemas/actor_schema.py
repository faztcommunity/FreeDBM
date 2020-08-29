#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.schemas import ma
from app.schemas.movie_schema import ActorGetMovieSchema


class ActorSchema(ma.Schema):

    movie_actors = ma.Nested(ActorGetMovieSchema, many=True)

    class Meta:
        fields = ('id', 'fullname', 'movie_actors')


# TODO(jsgonzlez661): Get one actor
schema_actor = ActorSchema()
# TODO(jsgonzlez661): Get all actors
schemas_actor = ActorSchema(many=True)
