from flask import Flask, request, render_template, jsonify
from bson.json_util import dumps
from logging.handlers import RotatingFileHandler
from pprint import pprint
from pymongo import MongoClient

import json
import logging
import time
import collections


client = MongoClient('localhost', 27017)
db = client['delivery_malli']
print("safasf")
x = db.packages.find(projection={'_id': True,'packageType':True})
print(x)
print(dumps(x))


print(x)