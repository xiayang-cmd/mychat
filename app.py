from flask import Flask, request, jsonify, render_template, Response
import requests
import json
import os

app = Flask(__name__)

@app.route('/')  # 修改为根路径
def index():  # 通常根路径的视图函数命名为index
    return 'Hello, World! This is your endpoint.'

@app.route('/hello', methods=['GET'])  # 定义GET方法
def hello():
    return '呵呵呵呵'  # 返回指定字符串

if __name__ == '__main__':
    app.run(port=5000)
