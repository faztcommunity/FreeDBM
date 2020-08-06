#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from flask import Flask
from flask_restful import Api
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from app.models import db
import config

app = Flask(__name__)

# TODO(jsgonzlez661): Load development mode
app.config.from_object(config.DevelopmentConfig)

CORS(app)  # TODO(jsgonzlez661): Configure cross-origin resource sharing

api = Api(app)
migrate = Migrate(app, db)  # TODO(jsgonzlez661): Flask-Migrate Configuration

manager = Manager(app)  # TODO(jsgonzlez661): Flask-Script Configuration
manager.add_command('db', MigrateCommand)

from .routes.signup import Signup
from .routes.login import Login
from .routes.get_new_token import Token
# TODO(jsgonzlez661): Register resource signup
api.add_resource(Signup, '/v1/auth/signup')
api.add_resource(Login, '/v1/auth/login')
api.add_resource(Token, '/v1/auth/token')
