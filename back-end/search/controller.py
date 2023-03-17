from search import db
import requests
import re
from flask import jsonify, request, session, json
from bson import json_util

def getMongo(dish):
    # 链接 MongoDB atlas
    myquery = {"title": dish}  # 查询条件
    mydoc = db.find(myquery)  # 查询结果
    print(mydoc)
    # 取出其中的数据格式为json
    for x in mydoc:
        # 将x转换为对象
        x = json.loads(json_util.dumps(x))
        print(x)
        return x
