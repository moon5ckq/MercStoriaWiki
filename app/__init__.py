#!encoding=utf-8
from flask import Flask
from foundation import db

app_ = Flask(__name__)
app_.config.from_object('config')

db.init_app(app_)
db.app = app_

import models
import views
