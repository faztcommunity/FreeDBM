#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.routes import *


class Signup(Resource):

    def get(self):  # TODO(jsgonzlez661): Method GET for route Signup
        # TODO(jsgonzlez661): Get params data user
        username = request.args.get('username', None)
        email = request.args.get('email', None)
        password = request.args.get('password', None)
        if(username != None and email != None and password != None):
            return Signup.user_email_check(username, email, password)
        return JSON.load_json('error_data'), 400

    def post(self):  # TODO(jsgonzlez661): Method POST for route Signup
        # TODO(jsgonzlez661): Load file json of request
        json_file = request.get_json(force=True)
        if(Responds.validate_json(json_file, 'user')):
            username = json_file.get('username', None)
            email = json_file.get('email', None)
            password = json_file.get('password', None)
            return Signup.user_email_check(username, email, password)
        return JSON.load_json('error_data'), 400

    @classmethod  # TODO(jsgonzlez661): Check data user
    def user_email_check(cls, username, email, password):
        if(User.get_by_email(email)):  # TODO(jsgonzlez661): Return message error email
            return JSON.load_json('error_email'), 401
        elif(User.get_by_username(username)):  # TODO(jsgonzlez661): Check username unique
            return JSON.load_json('error_username'), 401
        else:  # TODO(jsgonzlez661): Add user in DB
            User.create_element(username, email, password)
            return Responds.get_message_signup(username, email, password), 201
