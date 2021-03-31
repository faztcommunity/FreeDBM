#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Fazt Community ~ All rights reserved. MIT license.

from rest_framework.views import APIView
from rest_framework.response import Response
from movies.serializers import DirectorSerializer, MovieSerializer
from movies.models import Director
from .movie_view import Movie
from rest_framework.permissions import IsAuthenticated


class DirectorView(APIView):

    # TODO(jsgonzlez661): Check if the token is valid
    permission_classes = [IsAuthenticated]

    # TODO(jsgonzlez661): Get all data for director
    def get(self, request, *args, **kwargs):

        directors = Director.objects.all()

        if directors:
            # TODO(jsgonzlez661): Serializer data
            directors_serializer = DirectorSerializer(directors, many=True)
            return Response(directors_serializer.data, 200)

        data = {
            "status": 200,
            "message": "Empty database"
        }
        return Response(data, data['status'])


class DirectorIdView(APIView):

    # TODO(jsgonzlez661): Check if the token is valid
    permission_classes = [IsAuthenticated]

    # TODO(jsgonzlez661): Get data for director id
    def get(self, request, id=None, *args, **kwargs):

        director = Director.objects.filter(id=id)

        if director:
            movie = Movie.objects.filter(director__in=director)
            # TODO(jsgonzlez661): Serializer data
            director_serializer = DirectorSerializer(director, many=True)
            movie_serializer = MovieSerializer(movie, many=True)

            data = {
                'director': director_serializer.data,
                'movies': movie_serializer.data
            }
            return Response(data, 200)

        data = {
            "status": 200,
            "message": "No director with that id"
        }
        return Response(data, data['status'])
