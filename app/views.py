# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 mlckq <moon5ckq@gmail.com>
#
# Distributed under terms of the MIT license.
from app import app_
from flask import render_template, jsonify, request
from sqlalchemy import or_
from app.foundation import db
from app.models import Friend
import json

@app_.route('/')
def index():
    cols = ('dev_type', 'country', 'atk_type', 'rarity', 'type')
    cols_map = {
        'dev_type' : u'成长类型',
        'country' : u'国家',
        'atk_type' : u'攻击类型',
        'rarity' : u'稀有度',
        'type' : u'属性'
    }
    rst = Friend.query.with_entities(Friend.dev_type,\
            Friend.country, Friend.atk_type,\
            Friend.rarity, Friend.type).all()
    rst = map(set, zip(*rst))
    
    fltr = {}
    for i, k in enumerate(cols):
        fltr[k] = rst[i]

    return render_template('index.html', fltr=fltr, cols=cols_map)

@app_.route('/query', methods=['POST','GET'])
def query():
    querys = request.get_json(force=True)
    q = Friend.query
    for k, values in querys.iteritems():
        one_filter = []
        for v in values:
            one_filter.append(getattr(Friend, k) == v)
        q = q.filter(or_(*one_filter))
    ret = []
    for fri in q.all():
        ret.append({
            'id' : fri.id,
            'name' : fri.name,
            'name_' : fri.name.replace(u'」', u'」<br/>'),
            'type' : fri.type,
            'rarity' : fri.rarity,
            'rarity_' : "★" * fri.rarity,
            'hp' : fri.hp,
            'atk' : fri.atk,
            'dev_type' : fri.dev_type,
            'atk_nums' : fri.atk_nums,
            'cd' : fri.cd,
            'range' : fri.range
        });
    return jsonify({'result' : ret})

@app_.route('/friend/<int:friend_id>')
def friend(friend_id):
    fri = Friend.query.get_or_404(friend_id)
    correction = fri.correction.split(',')
    return render_template('friend.html', fri = fri, correction = correction)
