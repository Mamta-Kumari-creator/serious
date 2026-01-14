class config:
    SECRET_KEY = '125053'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
from controller.database import db
from flask import Flask
from controller.config import config