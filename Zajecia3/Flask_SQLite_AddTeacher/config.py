import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///example1.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'