# coding=utf-8
from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route('/')
def Home():
    data = json.dumps({
        "username": "admin",
        "password": "123456"
    })
    return data


@app.route('/passport/user/login', methods=['GET'])
def Login():

    username = request.args.get('username')
    password = request.args.get('password')
    if username and password:
        data = json.dumps({
            "username": username,
            "password": password,
            "code": "200",
            "message": "登陆成功"
        }, ensure_ascii=False)
    else:
        data = json.dumps({
            "message": "参数不能为空"
        }, ensure_ascii=False)
    return data


@app.route('/passport/user/post_login', methods=['POST'])
def post_login():
    request_method = request.method

    if request_method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        data = json.dumps({
            "username": username,
            "password": password,
            "code": "200",
            "message": "登陆成功"
        }, ensure_ascii=False)
    else:
        data = json.dumps({
            "message": "参数不能为空"
        }, ensure_ascii=False)

    return data


if __name__ == "__main__":
    app.run()
