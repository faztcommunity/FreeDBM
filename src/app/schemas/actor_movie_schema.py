#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.schemas import ma


# TODO(jsgonzlez661): Schema Get actor for movies
class ActorMovieSchema(ma.Schema):

    class Meta:
        fields = ('id', 'fullname')
