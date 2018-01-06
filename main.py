from flask import Flask, request, render_template, jsonify
from bson.json_util import dumps
from logging.handlers import RotatingFileHandler
from pprint import pprint
from pymongo import MongoClient

import json
import logging
import time
import collections
app = Flask(__name__)
global db
client = MongoClient('localhost', 27017)
db = client['code_new_world']


@app.route('/')
def hello_world():
    print("safasf")
    x = db.characters.find(projection={'_id': True,'name':True})
    print(x)
    return "/"

@app.route('/characterList',methods=['GET'])
def characterList():
    return dumps(db.characters.find(projection={'_id': True,'name':True}))

@app.route('/character/<id>',methods=['GET'])
def characterDeatils(id):
    return dumps(db.characters.find({'_id':id}))

@app.route('/createCharacter',methods=['POST'])
def createCharacter():
    print(request.get_json())
    print(dumps(request.get_json()))
    db.characters.insert_one(dumps(request.get_json()))
    return dumps(x)
   