from search import app, db
from flask import jsonify, request, session
from search.controller import getMongo


# route for home page
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/test', methods=['GET','POST'])
def test():
    return_dict = {'msg': '处理成功'}
    # 判断入参是否为空
    if request.method == "POST":
        post_data = request.get_json()
        print(post_data)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    dish = post_data.get('dish')
    print(dish)
    result = getMongo(dish)
    # 对参数进行操作
    return jsonify(result)
