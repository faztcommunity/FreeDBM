#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.routes import *


class Login(Resource):

    def post(self):  # TODO(jsgonzlez661): Method POST for route Login
        json_file = request.get_json(force=True)

        if(Responds.validate_json(json_file, 'login')):
            auth_token = json_file.get('auth_token', None)
            try:
                decoded = Login.validate_token(auth_token)
                email = decoded['user_data']['email']
                password = decoded['user_data']['password'].encode('utf-8')
            except:
                return decoded

            if(User.check_password(email, password)):  # TODO(jsgonzlez661): Check user's credentials
                responds = {
                    "responds": JSON.load_json('success_login'),
                    "auth_token": auth_token
                }
                cookie = make_response(responds)
                # TODO(jsgonzlez661): Make Cookie
                cookie.set_cookie("auth_token", auth_token)
                return cookie

            return JSON.load_json('error_email_password')
        return JSON.load_json('error_data')

    @classmethod
    # TODO(jsgonzlez661): Validate token
    def validate_token(cls, auth_token):
        try:
            decoded = jwt.decode(auth_token, config.KEY, algorithm='HS256')
        except jwt.exceptions.DecodeError:
            # TODO(jsgonzlez661): If token no validate
            return JSON.load_json('error_token')
        except jwt.ExpiredSignatureError:
            # TODO(jsgonzlez661): Check if token expire
            return JSON.load_json('error_token_expire'), 401

        return decoded
