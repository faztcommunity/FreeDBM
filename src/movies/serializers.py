#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Fazt Community ~ All rights reserved. MIT license.

from rest_framework import serializers
from .models import Movie, Gener, Actor, Director


# TODO(jsgonzlez661): Definition of serializers for movie urls

class GenerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gener
        fields = ['id', 'genere_name']


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ['id', 'fullname']


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ['id', 'fullname']


class MovieSerializer(serializers.ModelSerializer):

    # TODO(jsgonzlez661): Get data for movies
    genre = GenerSerializer(many=True, read_only=True)
    director = DirectorSerializer(many=True, read_only=True)
    actor = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'year', 'runtime', 'poster', 'synopsis', 'genre', 'director', 'actor', 'imdb_rating'
        ]
