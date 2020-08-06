#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

import json


class JSON():

    @classmethod
    def load_json(cls, nameJSON):
        with open("app\\json\\" + nameJSON + ".json") as json_file:
            return json.load(json_file)
