#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Fazt Community ~ All rights reserved. MIT license.

from rest_framework.views import APIView
from rest_framework.response import Response
from movies.serializers import MovieSerializer
from movies.models import Movie
from rest_framework.permissions import IsAuthenticated


class MovieView(APIView):

    # TODO(jsgonzlez661): Check if the token is valid
    permission_classes = [IsAuthenticated]

    # TODO(jsgonzlez661): Get all data for movie
    def get(self, request, *args, **kwargs):

        movies = Movie.objects.all()  # .order_by('-date_joined')

        if movies:
            # TODO(jsgonzlez661): Serializer data
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data, 200)

        data = {
            "status": 200,
            "message": "Empty database"
        }
        return Response(data, data['status'])


class MovieIdView(APIView):

    # TODO(jsgonzlez661): Check if the token is valid
    permission_classes = [IsAuthenticated]

    # TODO(jsgonzlez661): Get data for movie id
    def get(self, request, id=None, *args, **kwargs):

        movie = Movie.objects.filter(id=id)  # .order_by('-date_joined')

        if movie:
            # TODO(jsgonzlez661): Serializer data
            movie_serializer = MovieSerializer(movie, many=True)
            return Response(movie_serializer.data, 200)

        data = {
            "status": 200,
            "message": "No movie with that id"
        }
        return Response(data, data['status'])
