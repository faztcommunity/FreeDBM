# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

# TODO(jsgonzlez661): Configuration file for development or production mode

class BaseConfig(object): # TODO(jsgonzlez661): Basic mode settings
	SECRET_KEY = b"k\xec\xa6@\x8b7'\xb8\x0c>9\xd9\xcc\xc2 \xb5"	
	SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(BaseConfig): # TODO(jsgonzlez661): Configuration for the development mode
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:@127.0.0.1:3306/login_token' # TODO(jsgonzlez661): URI database for development 
	DEBUG = True

class ProductionConfig(BaseConfig): # TODO(jsgonzlez661): Configuration for the production mode
	SQLALCHEMY_DATABASE_URI = '' # TODO(jsgonzlez661): URI database for production 
	DEBUG = False
