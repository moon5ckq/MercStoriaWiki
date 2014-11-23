# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 mlckq <moon5ckq@gmail.com>
#
# Distributed under terms of the MIT license.

from app.foundation import db

class Friend(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    cn_name = db.Column(db.Text)
    atk_nums = db.Column(db.Integer)
    dev_type = db.Column(db.Text)
    country = db.Column(db.Text)
    correction = db.Column(db.Text)
    atk_type = db.Column(db.Text)
    rarity = db.Column(db.Integer)
    type = db.Column(db.Text)
    toughness = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    atk = db.Column(db.Integer)
    cd = db.Column(db.Float)
    range = db.Column(db.Integer)
    speed = db.Column(db.Integer)

