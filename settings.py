import os
import sqlite3

SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS=False

ADMIN_USERNAME=os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD=os.environ.get('ADMIN-PASSWORD')

 