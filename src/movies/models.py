#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Fazt Community ~ All rights reserved. MIT license.

# from django.contrib.auth import get_user_model
# User = get_user_model()
from django.db import models

# TODO(jsgonzlez661): Models for movies


class Gener(models.Model):

    genere_name = models.CharField(max_length=250, null=False, unique=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.genere_name


class Director(models.Model):

    fullname = models.CharField(max_length=250, null=False, unique=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class Actor(models.Model):

    fullname = models.CharField(max_length=250, null=False, unique=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class Movie(models.Model):

    title = models.CharField(max_length=250, null=False, unique=True)
    year = models.CharField(max_length=100, null=False)
    runtime = models.IntegerField(null=False)
    poster = models.CharField(max_length=250, null=False)
    synopsis = models.TextField()
    imdb_rating = models.CharField(max_length=50, null=False)
    genre = models.ManyToManyField(Gener)
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title
