#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from flask import request
from flask_restful import Resource
from app import api
from app.models.create_users_table import User
from cerberus import Validator
from app.schemas.json_schemas import user_schema
from app.schemas.json_schemas import success_signup_schema
import config
import jwt


class Responds():

    @classmethod
    def get_message_signup(cls, json_file):
        encoded_jwt = jwt.encode(json_file, config.KEY, algorithm='HS256')
        responds = {
            # TODO(jsgonzlez661): Make Token
            "auth_token": encoded_jwt.decode("utf-8"),
            "responds": success_signup_schema
        }
        return responds

    @classmethod
    # TODO(jsgonzlez661): Validate schema json for signup
    def validate_json_signup(cls, json_file):
        v = Validator()
        return v.validate(json_file, user_schema)
