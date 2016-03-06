# _*_ coding=utf-8 _*_
__author__ = 'patrick'

from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Flask World"


@app.route('/appconfig')
def config():
    return app.config['DEBUG']


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

# int 整数
# float 浮点数
# path 接受斜线
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/projects')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'This is about page'

@app.route("/achieve")
def achieve():
    return "this is archieve"


# Http methods: GET/POST/DELETE/HEAD/OPTIONS/PUT
@app.route('/login', methods={'GET', 'POST'})
def login():
    if request.method == 'POST':
        print "login successfully"
    else:
        print "login"


if __name__ == '__main__':
    app.run(debug=True)
    with app.test_request_context():
        print url_for(achieve)
