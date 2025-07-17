import os

DB_USER = 'root'
DB_PASSWORD = 'maro1234'
DB_HOST = 'localhost'
DB_NAME = 'notesdb'

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(24)
