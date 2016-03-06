# _*_ coding=utf-8 _*_
import sqlite3
import os
from flask import Flask, g, render_template, session, abort, \
    flash, request, redirect, url_for

__author__ = 'patrick'


# create app
app = Flask(__name__)

# load default config and override config from environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'blog.db'),
    DEBUG=True,
    USERNAME='patrick',
    PASSWORD='password'
))

app.config.from_envvar('FLASK_SETTINGS', silent=True)


def connect_db():
    """connect to the database"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """open a new database connect"""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def init_db():
    """initializes the database create tables"""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """create tabalse tables"""
    init_db()
    print("initialized the database.")


@app.teardown_appcontext
def close_db(error):
    """close the database again at the end of request"""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('SELECT title,text FROM entries ORDER BY id DESC')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
        db = get_db()
        db.execute('INSERT INTO entries (title, text) VALUES (?, ?)',
                   [request.form['title'], request.form['text']])
        db.commit()
        flash('New entry was successfully posted')
        return redirect(url_for('show_entries'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
