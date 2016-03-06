# _*_ coding=utf-8 _*_
__author__ = 'patrick'


import pytest
import os
import blog
import tempfile

@pytest.fixture
def client(request):
    db_fd,blog.app.config['DATABASE'] = tempfile.mktemp()
    blog.app.config['TESTING'] = True
    client=blog.app.test_client()
    with blog.app.app_context():
        blog.init_db()

    def teardown():
        os.close(db_fd)
        os.unlink(blog.app.config['DATABASE'])

    request.addfinalizer(teardown())

def login(client,username,password):
    return client.post('blog',data=dict(
        usernmae=username,
        password=password
    ),follow_redirects =True)


def logout(client):
    return client.get('/logout',follow_redirects=True)


def test_empty_db(client):
    rv = client.get("/")
    assert b'No Entries here so far' in rv.data


def test_login_logout(client):
    rv =login(client,blog.app.config['username'])
    assert b'You Were logged in' in rv.data

    rv=logout(client)
    assert b'You were logged out' in rv.data

    rv = login(client, blog.app.config['USERNAME'] + 'x',
               blog.app.config['PASSWORD'])
    assert b'Invalid username' in rv.data
    rv = login(client, blog.app.config['USERNAME'],
               blog.app.config['PASSWORD'] + 'x')
    assert b'Invalid password' in rv.data


def test_messages(client):
    """Test that messages work"""
    login(client, blog.app.config['USERNAME'],
          blog.app.config['PASSWORD'])
    rv = client.post('/add', data=dict(
        title='<Hello>',
        text='<strong>HTML</strong> allowed here'
    ), follow_redirects=True)
    assert b'No entries here so far' not in rv.data
    assert b'&lt;Hello&gt;' in rv.data
    assert b'<strong>HTML</strong> allowed here' in rv.data