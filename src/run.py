#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

# TODO(jsgonzlez661): File to start the server

from app import app, manager
from app.models import db

if __name__ == '__main__':

    db.init_app(app)  # TODO(jsgonzlez661): Load database in app
    with app.app_context():
        db.create_all()  # TODO(jsgonzlez661): Make all tables

    manager.run()  # TODO(jsgonzlez661): Migration configuration
