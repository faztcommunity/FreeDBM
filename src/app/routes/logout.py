#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.routes import *


class Logout(Resource):

    def get(self):
        cookies = request.cookies  # TODO(jsgonzlez661): Get cookies
        if(cookies != {}):
            response = make_response(JSON.load_json('success_logged_out'))
            # TODO(jsgonzlez661): Delete cookies
            response.delete_cookie('auth_token')
            return response
        else:
            return JSON.load_json('user_not_login'), 200
