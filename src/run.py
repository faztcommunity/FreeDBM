# Copyright 2020 Fazt Community ~ All rights reserved. MIT license.

# TODO(jsgonzlez661): File to start the server

from app import app 
from app.models import db  

if __name__ == '__main__':
	db.init_app(app) 
	with app.app_context():
		db.create_all()
	app.run()  