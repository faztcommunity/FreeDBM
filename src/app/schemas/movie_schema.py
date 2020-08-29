#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.schemas import ma
from app.schemas.director_movie_schema import DirectorMovieSchema
from app.schemas.actor_movie_schema import ActorMovieSchema
from app.schemas.genre_movie_schema import GenreMovieSchema


class MovieSchema(ma.Schema):

    director = ma.Nested(DirectorMovieSchema, many=True)
    actor = ma.Nested(ActorMovieSchema, many=True)
    genre = ma.Nested(GenreMovieSchema, many=True)

    class Meta:
        fields = ('id', 'title', 'year', 'runtime', 'genre',
                  'director', 'actor', 'synopsis', 'imdb_rating', 'poster')

# TODO(jsgonzlez661): Get one movie
schema_movie = MovieSchema()
# TODO(jsgonzlez661): Get all movies
schema_movies = MovieSchema(many=True)


class DirectorGetMovieSchema(ma.Schema):

    actor = ma.Nested(ActorMovieSchema, many=True)
    genre = ma.Nested(GenreMovieSchema, many=True)

    class Meta:
        fields = ('id', 'title', 'year', 'runtime', 'genre',
                  'actor', 'synopsis', 'imdb_rating', 'poster')


class ActorGetMovieSchema(ma.Schema):

    director = ma.Nested(DirectorMovieSchema, many=True)
    genre = ma.Nested(GenreMovieSchema, many=True)

    class Meta:
        fields = ('id', 'title', 'year', 'runtime', 'genre',
                  'director', 'synopsis', 'imdb_rating', 'poster')


class GenreGetMovieSchema(ma.Schema):

    director = ma.Nested(DirectorMovieSchema, many=True)
    actor = ma.Nested(ActorMovieSchema, many=True)

    class Meta:
        fields = ('id', 'title', 'year', 'runtime', 'director',
                  'actor', 'synopsis', 'imdb_rating', 'poster')
