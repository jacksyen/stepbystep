# _*_ coding=utf-8 _*_
__author__ = 'patrick'

from flask import render_template, request
from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] != "":
            return render_template('hello.html', 'patrick')
        else:
            error = 'Invalid user'
            return render_template('hello.html', error)
    else:
        return render_template('hello.html', request.args.get('login', ''))
    return render_template('hello.html', 'GET')

@app.route('/index/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()