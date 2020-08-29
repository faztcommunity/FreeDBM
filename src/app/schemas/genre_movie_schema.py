#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.schemas import ma


# TODO(jsgonzlez661): Get genre for movies
class GenreMovieSchema(ma.Schema):

    class Meta:
        fields = ('id', 'genere_name')
