#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Fazt Community ~ All rights reserved. MIT license.

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from register.serializers import SignupSerializer


class SignupView(APIView):

    # TODO(jsgonzlez661): Method POST for data user
    def post(self, request, *args, **kwargs):

        # TODO(jsgonzlez661): Validate unique data user in database
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            # TODO(jsgonzlez661): Encrypt password
            hashed = make_password(password)
            user = User(username=username, email=email,
                        password=hashed)
            user.save()
            token, _ = Token.objects.get_or_create(user=user)

            data = {
                "user_data": {
                    'username': username,
                    'email': email,
                },
                'token': token.key,
                "status": 201,
                "message": "Successfully registered"
            }
            return Response(data, data['status'])
        data = {
            'status': 401,
            'message': serializer.errors,
        }
        return Response(data, data['status'])
