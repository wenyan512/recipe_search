from search import app, db, model, tokenizer, seq_len, num_gen_words
from flask import jsonify, request, session
from search.controller import getMongo, gen_text


# route for home page
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/test', methods=['GET','POST'])
def test():
    # 判断入参是否为空
    if request.method == "POST":
        post_data = request.get_json()
    # 获取传入的params参数
    dish = post_data.get('dish')
    print(dish)
    result = getMongo(dish)
    # 对参数进行操作
    return jsonify(result)

@app.route('/suggestion', methods=['GET', 'POST'])
def suggestion():
    if request.method == "POST":
        post_data = request.get_json()
    seed_text = post_data.get('input')
    result = []
    if (seed_text != ''):
        for i in range(-3,0):
            out = gen_text(model, tokenizer, seq_len=seq_len, seed_text=seed_text, num_gen_words=num_gen_words, first=i)
            print('Output: '+seed_text+' '+out)
            result.append(seed_text+' '+out)
    return jsonify({'suggestion': result})
