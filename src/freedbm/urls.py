#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Fazt Community ~ All rights reserved. MIT license.

from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

# TODO(jsgonzlez661): Import urls of my apss
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),
    path('', include('register.urls')),

]

urlpatterns = format_suffix_patterns(urlpatterns)
