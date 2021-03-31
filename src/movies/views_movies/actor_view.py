#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Fazt Community ~ All rights reserved. MIT license.

from rest_framework.views import APIView
from rest_framework.response import Response
from movies.serializers import ActorSerializer, MovieSerializer
from movies.models import Actor
from .movie_view import Movie
from rest_framework.permissions import IsAuthenticated


class ActorView(APIView):
    # TODO(jsgonzlez661): Check if the token is valid
    permission_classes = [IsAuthenticated]

    # TODO(jsgonzlez661): Get all data for actor
    def get(self, request, *args, **kwargs):

        actors = Actor.objects.all()

        if actors:
            # TODO(jsgonzlez661): Serializer data
            actors_serializer = ActorSerializer(actors, many=True)

            return Response(actors_serializer.data, 200)

        data = {
            "status": 200,
            "message": "Empty database"
        }
        return Response(data, data['status'])


class ActorIdView(APIView):

    # TODO(jsgonzlez661): Check if the token is valid
    permission_classes = [IsAuthenticated]

    # TODO(jsgonzlez661): Get data for actor id
    def get(self, request, id=None, *args, **kwargs):

        actor = Actor.objects.filter(id=id)

        if actor:
            movie = Movie.objects.filter(actor__in=actor)

            # TODO(jsgonzlez661): Serializer data
            actor_serializer = ActorSerializer(actor, many=True)
            movie_serializer = MovieSerializer(movie, many=True)

            data = {
                'status': 200,
                'actor': actor_serializer.data,
                'movies': movie_serializer.data
            }
            return Response(data, data['status'])

        data = {
            "status": 200,
            "message": "No actor with that id"
        }
        return Response(data, data['status'])
