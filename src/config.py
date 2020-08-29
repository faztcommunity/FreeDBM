#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

# TODO(jsgonzlez661): Configuration file for development or production mode
import os

KEY = b"k\xec\xa6@\x8b7'\xb8\x0c>9\xd9\xcc\xc2 \xb5"


class BaseConfig(object):  # TODO(jsgonzlez661): Basic mode settings
    SECRET_KEY = KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # TODO(jsgonzlez661): Configuration for Flask - Mail send mail
    # TODO(jsgonzlez661): Mail Server Here
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    # TODO(jsgonzlez661): Email Here
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    # TODO(jsgonzlez661): Password Here
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    # TODO(jsgonzlez661): Username and email Here
    DONT_REPLY_FROM_EMAIL = os.getenv('DONT_REPLY_FROM_EMAIL')
    ADMINS = os.getenv('ADMINS')  # TODO(jsgonzlez661): Email Here
    MAIL_USE_TLS = True


# TODO(jsgonzlez661): Configuration for the development mode
class DevelopmentConfig(BaseConfig):
    # TODO(jsgonzlez661): URI database for development
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:@127.0.0.1:3306/freedbm_data'
    DEBUG = True


# TODO(jsgonzlez661): Configuration for the production mode
class ProductionConfig(BaseConfig):
    # TODO(jsgonzlez661): URI database for production
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    DEBUG = False
