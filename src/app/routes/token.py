#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.routes import *


class Token(Resource):  # TODO(jsgonzlez661): Generate a new token

    def post(self):  # TODO(jsgonzlez661): Method POST for route Token
        json_file = request.get_json(force=True)
        if(Responds.validate_json(json_file, 'user_token')):
            email = json_file.get('email', None)
            password = json_file.get('password', None)
            return Responds.get_new_token(email, password)
        return JSON.load_json('error_data'), 400
