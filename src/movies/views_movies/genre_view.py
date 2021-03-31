#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Fazt Community ~ All rights reserved. MIT license.

from rest_framework.views import APIView
from rest_framework.response import Response
from movies.serializers import GenerSerializer, MovieSerializer
from movies.models import Gener
from .movie_view import Movie
from rest_framework.permissions import IsAuthenticated


class GenerView(APIView):

    # TODO(jsgonzlez661): Check if the token is valid
    permission_classes = [IsAuthenticated]

    # TODO(jsgonzlez661): Get all data for genre
    def get(self, request, *args, **kwargs):

        geners = Gener.objects.all()

        if geners:
            # TODO(jsgonzlez661): Serializer data
            geners_serializer = GenerSerializer(geners, many=True)
            return Response(geners_serializer.data, 200)

        data = {
            "status": 200,
            "message": "Empty database"
        }
        return Response(data, data['status'])


class GenerIdView(APIView):

    # TODO(jsgonzlez661): Check if the token is valid
    permission_classes = [IsAuthenticated]

    # TODO(jsgonzlez661): Get data for genre id
    def get(self, request, id=None, *args, **kwargs):

        genre = Gener.objects.filter(id=id)  # .order_by('-date_joined')

        if genre:
            # TODO(jsgonzlez661): Serializer data
            movie = Movie.objects.filter(genre__in=genre)
            genre_serializer = GenerSerializer(genre, many=True)
            movie_serializer = MovieSerializer(movie, many=True)

            data = {
                'genre': genre_serializer.data,
                'movies': movie_serializer.data
            }
            return Response(data, 200)

        data = {
            "status": 200,
            "message": "No gender with that id"
        }
        return Response(data, data['status'])
