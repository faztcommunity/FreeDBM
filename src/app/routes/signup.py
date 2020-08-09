#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.routes import *


class Signup(Resource):

    def post(self):  # TODO(jsgonzlez661): Method POST for route Signup
        # TODO(jsgonzlez661): Load file json of request
        json_file = request.get_json(force=True)
        if(Responds.validate_json(json_file, 'user')):
            username = json_file.get('username', None)
            email = json_file.get('email', None)
            password = json_file.get('password', None)

            if(User.get_by_email(email)):  # TODO(jsgonzlez661): Return message error email
                return JSON.load_json('error_email'), 401
            elif(User.get_by_username(username)):  # TODO(jsgonzlez661): Check username unique
                return JSON.load_json('error_username'), 401
            else:  # TODO(jsgonzlez661): Add user in DB
                User.create_element(username, email, password)
                return Responds.post_message_signup(json_file), 201
        return JSON.load_json('error_data'), 400
