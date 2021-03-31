#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Fazt Community ~ All rights reserved. MIT license.

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from register.serializers import TokenSerializer


class TokenView(ObtainAuthToken):

    # TODO(jsgonzlez661): Method POST for token view
    def post(self, request, *args, **kwargs):

        # TODO(jsgonzlez661): Validate data user
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():

            user = serializer.validated_data['user']
            # TODO(jsgonzlez661): Get Token
            token = Token.objects.get(user_id=user.id)
            token_serializer = TokenSerializer(token)

            data = {
                'Token': token_serializer.data['key'],
                'username': user.username,
                'status': 200,
                'message': 'This is your token'
            }
            return Response(data, data['status'])

        data = {
            'status': 401,
            'message': serializer.errors['non_field_errors'][0]
        }
        return Response(data, data['status'])
