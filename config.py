#! encoding=utf-8
import os, datetime, time
basedir = os.path.abspath(os.path.dirname(__file__))

SQLITE_DATABASE_NAME = 'mercstoria.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, SQLITE_DATABASE_NAME)

CSRF_ENABLED = True

