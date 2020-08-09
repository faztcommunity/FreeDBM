#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from flask import request, make_response, url_for
from flask_restful import Resource
from app import api
from app.models.create_users_table import User
from app.models import db
from cerberus import Validator
from app.json import JSON
from sqlalchemy.sql import select
import config
import jwt
import datetime


class Responds():

    @classmethod
    def post_message_signup(cls, json_file):
        file_json = {
            'user_data': json_file,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=86400)
        }
        # TODO(jsgonzlez661): Time expiration for 24 hours
        encoded_jwt = jwt.encode(file_json, config.KEY, algorithm='HS256')
        responds = {
            # TODO(jsgonzlez661): Make Token
            "auth_token": encoded_jwt.decode("utf-8"),
            "responds": JSON.load_json('success_signup'),
            "login": "/v1/auth/login"
        }
        return responds

    @classmethod
    # TODO(jsgonzlez661): Validate schema json
    def validate_json(cls, json_file, name_file):
        v = Validator()
        return v.validate(json_file, JSON.load_json(name_file))

    @classmethod
    # TODO(jsgonzlez661): Generate new token
    def get_new_token(cls, email, password):

        if(User.get_by_email(email)):
            query = select([User]).where(User.email == email)
            result = db.session.execute(query)
            user = result.fetchone()
            if(user != None and len(user) > 0):
                if(User.verify_password(user['encrypted_password'], password)):
                    file_json = {
                        'user_data': {
                            'username': user['username'],
                            'email': email,
                            'password': password
                        },
                        # TODO(jsgonzlez661): Time expiration for 24 hours
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=86400)
                    }
                    encoded_jwt = jwt.encode(
                        file_json, config.KEY, algorithm='HS256')
                    responds = {
                        "auth_token": encoded_jwt.decode("utf-8"),
                        "responds": JSON.load_json('success_token')
                    }
                    return responds
                return JSON.load_json('error_password')
            else:
                return JSON.load_json('error_email_check')
        return JSON.load_json('error_email_check')
