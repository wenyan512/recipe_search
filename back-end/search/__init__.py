from flask import Flask, jsonify
from flask import Flask, request, render_template, make_response, redirect, url_for
import json
from flask_cors import CORS
import pymongo
from bson import json_util

# connect database
# 数据库名称
myDataBase = "test"
# 集合名称
myCollection = "recipe"
# 数据库通信证,换成你自己的
tooken = "mongodb+srv://faye:passwordforttds@cluster0.d0myq6k.mongodb.net/?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(tooken)
mydb = myclient[myDataBase]  # 数据库名称
db = mydb[myCollection]  # 集合名称


app = Flask(__name__)
CORS(app, resources=r'/*')  # 注册 CORS, "/*" 允许访问所有api

from search import routes
