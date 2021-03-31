#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Fazt Community ~ All rights reserved. MIT license.

from django.contrib import admin
from .models import Movie, Actor, Director, Gener


# TODO(jsgonzlez661): Customization of data displayed in the django manager

class MovieAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'year', 'imdb_rating')

    filter_horizontal = ('genre', 'director', 'actor',)


class ActorAdmin(admin.ModelAdmin):

    list_display = ('id', 'fullname')


class DirectorAdmin(admin.ModelAdmin):

    list_display = ('id', 'fullname')


class GenerAdmin(admin.ModelAdmin):

    list_display = ('id', 'genere_name')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Gener, GenerAdmin)
