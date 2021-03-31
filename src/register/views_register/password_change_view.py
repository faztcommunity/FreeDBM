#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Fazt Community ~ All rights reserved. MIT license.

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework import status


class PasswordChangeView(ObtainAuthToken):

    # TODO(jsgonzlez661): Check if the token is valid
    permission_classes = [IsAuthenticated]

    # TODO(jsgonzlez661): Post data for change password
    def post(self, request, *args, **kwargs):

        # TODO(jsgonzlez661): Validate data user
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        if serializer.is_valid():
            new_password = request.POST.get('new_password')

            user = serializer.validated_data['user']
            user.password = make_password(new_password)
            user.save()

            data = {
                "status": 200,
                "message": "Successful password change"
            }

            return Response(data, data['status'])

        data = {
            'status': 401,
            'message': serializer.errors['non_field_errors'][0]
        }
        return Response(data, data['status'])
