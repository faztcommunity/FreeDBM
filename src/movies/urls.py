#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Fazt Community ~ All rights reserved. MIT license.

from django.urls import path
from .views import MovieView, MovieIdView, GenerView, GenerIdView, DirectorView, DirectorIdView, ActorView, ActorIdView

# TODO(jsgonzlez661): Specify the urls of movies
urlpatterns = [
    path('v2/movies/', MovieView.as_view()),
    path('v2/movie/<int:id>/', MovieIdView.as_view()),
    path('v2/geners/', GenerView.as_view()),
    path('v2/gener/<int:id>/', GenerIdView.as_view()),
    path('v2/directors/', DirectorView.as_view()),
    path('v2/director/<int:id>/', DirectorIdView.as_view()),
    path('v2/actor/', ActorView.as_view()),
    path('v2/actor/<int:id>/', ActorIdView.as_view()),
]
