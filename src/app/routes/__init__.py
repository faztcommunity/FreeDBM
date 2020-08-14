#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from flask import request, make_response, url_for
from flask_restful import Resource
from flask_mail import Message
from app import app, api, mail
from app.models.create_users_table import User
from app.models import db
from cerberus import Validator
from app.json import JSON
from sqlalchemy.sql import select
from werkzeug.security import generate_password_hash
from threading import Thread
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

    # TODO(jsgonzlez661): Send an email with the user data to have a backup
    @classmethod
    def send_message(cls, subject, username, email, password):
        msg = Message(subject, sender="jsgonzlez661@gmail.com",
                      recipients=[email])
        msg.html = "<h1>FreeDBM</h1><p>Thank you for registering</p><p><b>Username:</b> {0}<br><b>Email:</b> {1}<br><b>Password:</b> {2}</p><h4>Do not share this email</h4>".format(
            username, email, password)
        mail.send(msg)

    @classmethod
    def send_message_reset(cls, json_file):
        file_json = {
            'username': json_file.get('username', None),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)
        }
        email = json_file.get('email', None)
        url_jwt = jwt.encode(file_json, config.KEY, algorithm='HS256')

        msg = Message('Reset Password', sender="jsgonzlez661@gmail.com",
                      recipients=[email])
        msg.html = "<h1>FreeDBM</h1><p>You are receiving this email because you made a password recovery request</p><p>Follow the link to recover your password<br><br>http://localhost:5000/v1/auth/user/reset?key={0}</p><h4>This email expires in one hour</h4>".format(
            url_jwt.decode("utf-8"))
        mail.send(msg)
