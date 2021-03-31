#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Fazt Community ~ All rights reserved. MIT license.

from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# TODO(jsgonzlez661): Model serializer for validate register user
class SignupSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=250)
    password = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_username(self, value):
        data = self.get_initial()
        if User.objects.filter(username=data.get('username')).exists():
            raise ValidationError("There's already a user with that username")

    def validate_email(self, value):
        data = self.get_initial()
        if User.objects.filter(email=data.get('email')).exists():
            raise ValidationError("There's already a user with that email")
