#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.routes import *


class RecoveryPassword(Resource):  # TODO(jsgonzlez661): Recovery to user password

    def post(self):  # TODO(jsgonzlez661): Method POST for route
        json_file = request.get_json(force=True)
        if(Responds.validate_json(json_file, 'user_recovery_password')):
            username = json_file.get('username', None)
            email = json_file.get('email', None)
            if(User.get_by_email(email)):
                # TODO(jsgonzlez661): Send email with link reset password
                Responds.send_message_reset(json_file)
                return JSON.load_json('success_send_email'), 200
            else:
                return JSON.load_json('error_data'), 400
        else:
            return JSON.load_json('error_data'), 400
