#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Fazt Community ~ All rights reserved. MIT license.

from rest_framework import serializers
from rest_framework.authtoken.models import Token


# TODO(jsgonzlez661): Serializer token
class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ['key', ]
