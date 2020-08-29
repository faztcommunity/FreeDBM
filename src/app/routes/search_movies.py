#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.routes import *
from app.models import db
from app.models.create_director_table import Director
from app.models.create_actors_table import Actor
from app.models.create_genres_table import Gener
from app.models.create_users_table import User
from app.models.create_movies_table import Movie
from app.schemas.movie_schema import schema_movies
from app.schemas.director_schema import schemas_director
from app.schemas.actor_schema import schemas_actor
from app.schemas.genre_schema import schemas_genre


class SearchMovie(Resource):  # TODO(jsgonzlez661): Route for search movie in database

    def get(self):
        title = request.args.get('title', None)
        director = request.args.get('director', None)
        genre = request.args.get('genre', None)
        actor = request.args.get('actor', None)
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

            # TODO(jsgonzlez661): Search all movie for title
            if(title is not None):
                search = "%{}%".format(title)
                movies = Movie.query.filter(Movie.title.like(search)).all()
                return schema_movies.dump(movies), 200

            # TODO(jsgonzlez661): Search all movie for director
            elif(director is not None):
                search = "%{}%".format(director)
                movies = Director.query.filter(
                    Director.fullname.like(search)).all()
                return schemas_director.dump(movies), 200

            # TODO(jsgonzlez661): Search all movie for actor
            elif(actor is not None):
                search = "%{}%".format(actor)
                movies = Actor.query.filter(Actor.fullname.like(search)).all()
                return schemas_actor.dump(movies), 200

            # TODO(jsgonzlez661): Search all movie for genre
            elif(genre is not None):
                search = "%{}%".format(genre)
                genres_movie = Gener.query.filter(
                    Gener.genere_name.like(search)).all()
                return schemas_genre.dump(genres_movie), 200

        else:
            return JSON.load_json('user_not_login'), 200
