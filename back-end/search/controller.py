from search import db
import requests
import re
from flask import jsonify, request, session, json
from bson import json_util

from keras_preprocessing.sequence import pad_sequences
from keras.models import load_model
from pickle import load
import numpy as np
import os

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
    
def gen_text(model, tokenizer, seq_len, seed_text, num_gen_words, first):
    output_text = []
    input_text = seed_text
    for i in range(num_gen_words):
        encoded_text = tokenizer.texts_to_sequences([input_text])[0]
        pad_encoded = pad_sequences([encoded_text], maxlen=seq_len,truncating='pre')
        pred_word_ind = np.argsort(model.predict(pad_encoded))[-1][first]
        pred_word = tokenizer.index_word[pred_word_ind]
        input_text += ' '+pred_word
        output_text.append(pred_word)
    return ' '.join(output_text)