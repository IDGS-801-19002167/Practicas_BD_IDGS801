import os, urllib
from sqlalchemy import create_engine


class Config(object):
    SECRET_KEY = "Waza my nigga"
    SESSION_COOKIE_SECURE = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/practicas_bd"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
