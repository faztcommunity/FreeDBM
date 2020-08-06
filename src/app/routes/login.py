#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.routes import *


class Login(Resource):

    def post(self):
        json_file = request.get_json(force=True)

        if(Responds.validate_json_login(json_file)):
            auth_token = json_file.get('auth_token', None)
            try:
                # TODO(jsgonzlez661): Validate token
                decoded = jwt.decode(auth_token, config.KEY, algorithm='HS256')
            except jwt.exceptions.DecodeError:
                # TODO(jsgonzlez661): If token no validate
                return JSON.load_json('error_token')
            except jwt.ExpiredSignatureError:
                # TODO(jsgonzlez661): Check if token expire
                return JSON.load_json('error_token_expire'), 401

            email = decoded['user_data']['email']
            password = decoded['user_data']['password'].encode('utf-8')

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
