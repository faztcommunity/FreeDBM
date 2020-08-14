#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from app.routes import *
from .login import Login


class ResetPassword(Resource):  # TODO(jsgonzlez661): Reset to user password

    def put(self):  # TODO(jsgonzlez661): Method PUT for route
        key = request.args.get('key', None)  # TODO(jsgonzlez661): Get url key
        if(key != None):
            try:
                # TODO(jsgonzlez661): Validate key
                decoded = ResetPassword.validate_key(key)
                username = decoded['username']
            except:
                return decoded
            if(User.get_by_username(username)):
                json_file = request.get_json(force=True)
                if(Responds.validate_json(json_file, 'user_reset_password')):
                    new_password = json_file.get('new_password', None)
                    confirmed_password = json_file.get(
                        'confirmed_password', None)
                    # TODO(jsgonzlez661): Compare password
                    if(new_password == confirmed_password):
                        user = User.get_by_username(username)
                        user.encrypted_password = generate_password_hash(
                            new_password)
                        db.session.commit()
                        return JSON.load_json('success_new_password'), 200
                    else:
                        return JSON.load_json('error_password_equal'), 400
                else:
                    return JSON.load_json('error_data'), 400
            else:
                return JSON.load_json('error_data'), 400
        else:
            return JSON.load_json('error_key'), 401

    @classmethod
    # TODO(jsgonzlez661): Validate key
    def validate_key(cls, key):
        try:
            decoded = jwt.decode(key, config.KEY, algorithm='HS256')
        except jwt.exceptions.DecodeError:
            # TODO(jsgonzlez661): If key no validate
            return JSON.load_json('error_key')
        except jwt.ExpiredSignatureError:
            # TODO(jsgonzlez661): Check if key expire
            return JSON.load_json('error_key_expire'), 401

        return decoded
