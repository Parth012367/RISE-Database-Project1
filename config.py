# config.py
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'you-can-change-this-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'hospital.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
