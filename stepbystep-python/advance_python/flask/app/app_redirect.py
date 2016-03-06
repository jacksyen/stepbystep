# _*_ coding=utf-8 _*_
__author__ = 'patrick'

from flask import Flask,abort,redirect,url_for,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login/')
def login():
    abort(401)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('hello.html',error)

if __name__ == '__main__':
    app.run()