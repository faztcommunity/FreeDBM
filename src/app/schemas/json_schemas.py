#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

# TODO(jsgonzlez661): File json schemas

user_schema = {
    "username":
    {
        "type": "string",
        "min": 2,
        "max": 100
    },
    "email":
    {
        "type": "string",
        "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
    },
    "password":
    {
        "type": "string",
        "min": 8,
        "max": 94
    }
}

# TODO(jsgonzlez661): Message current mail
error_email_schema = {
    "status": "fail",
    "message": "There's already a user with that email"
}

# TODO(jsgonzlez661): Message username in use
error_username_schema = {
    "status": "fail",
    "message": "There's already a user with that username"
}

# TODO(jsgonzlez661): Message username or email invalid
error_data_schema = {
    "status": "fail",
    "message": "Invalid data"
}

# TODO(jsgonzlez661): Message successfully registered
success_signup_schema = {
    "status": "success",
    "message": "Successfully registered"
}
