#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.routes import *
from app.models.create_movies_table import Movie
from app.schemas.movie_schema import schema_movies


class AllMovies(Resource):  # TODO(jsgonzlez661): Route get all movies

    def get(self):
        cookies = request.cookies
        if(cookies != {}):
            # TODO(jsgonzlez661): Check token and validate
            try:
                token = jwt.decode(
                    cookies['auth_token'], config.KEY, algorithm='HS256')
            except jwt.exceptions.DecodeError:
                # TODO(jsgonzlez661): If token no validate
                return JSON.load_json('error_token')
            except jwt.ExpiredSignatureError:
                # TODO(jsgonzlez661): Check if key expire
                return JSON.load_json('error_key_expire'), 401

            # TODO(jsgonzlez661): Get all Movies
            movies = Movie.query.all()
            return schema_movies.dump(movies), 200

        else:
            return JSON.load_json('user_not_login'), 200
