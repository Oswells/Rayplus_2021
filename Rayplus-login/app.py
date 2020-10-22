from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash, session
from functools import wraps
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'PETLAB'
bootstrap = Bootstrap(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

users = [
    {
        'username': 'root',
        'password': 'root'
    },
]


@app.route('/')
def hello_world():
    return '欢迎登录!'


@app.route('/index')
def index():
    username = request.form.get('username')
    password = request.form.get('password')
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
