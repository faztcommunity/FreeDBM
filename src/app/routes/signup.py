#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.routes import *
from app.schemas.json_schemas import error_email_schema
from app.schemas.json_schemas import error_data_schema
from app.schemas.json_schemas import error_username_schema


class Signup(Resource):

    def post(self):  # TODO(jsgonzlez661): Method POST for route Signup
        # TODO(jsgonzlez661): Load file json of request
        json_file = request.get_json(force=True)
        username = json_file.get('username', None)
        email = json_file.get('email', None)
        password = json_file.get('password', None)

        if(Responds.validate_json_signup(json_file)):

            if(User.get_by_email(email)):
                # TODO(jsgonzlez661): Return message error email
                return error_email_schema, 401
            elif(User.get_by_username(username)):
                # TODO(jsgonzlez661): Check username unique
                return error_username_schema, 401
            else:
                # TODO(jsgonzlez661): Add user in DB
                User.create_element(username, email, password)
                return Responds.get_message_signup(json_file), 201

        return error_data_schema, 400
