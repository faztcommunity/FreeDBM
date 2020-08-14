#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.routes import *


class ChangePassword(Resource):  # TODO(jsgonzlez661): Change to user password

    def put(self):  # TODO(jsgonzlez661): Method PUT for route
        json_file = request.get_json(force=True)
        if(Responds.validate_json(json_file, 'user_new_password')):
            email = json_file.get('email', None)
            password = json_file.get('password', None)
            new_password = json_file.get('new_password', None)
            if(User.change_password(email, password, new_password)):
                return JSON.load_json('success_new_password'), 200
            else:
                return JSON.load_json('error_email_password'), 401
        else:
            return JSON.load_json('error_data'), 400
