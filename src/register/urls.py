#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Fazt Community ~ All rights reserved. MIT license.

from django.urls import path
from .views import SignupView, PasswordChangeView, TokenView

# TODO(jsgonzlez661): Define urls for apps register
urlpatterns = [
    path('v2/user/signup/', SignupView.as_view()),
    path('v2/user/password-change/', PasswordChangeView.as_view()),
    path('v2/user/token/', TokenView.as_view()),
]
