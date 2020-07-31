#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime

db = SQLAlchemy()

from .create_director_table import Director
from .create_actors_table import Actor
from .create_genres_table import Gener
from .create_users_table import User
from .create_movies_table import Movie
