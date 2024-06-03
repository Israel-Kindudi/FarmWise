import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "don't forget to encrypt this"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or 'sqlite:///farm.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    