# _*_ coding=utf-8 _*_
from werkzeug.wsgi import SharedDataMiddleware

__author__ = 'patrick'
import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/upload'
ALLOWED_EXTENSIONS = set(['txt', 'jpg', 'png','pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.add_url_rule('uploads/<file_name>','upload_file',build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app,{
    '/uploads': app.config['UPLOAD_FOLDER']
})
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024*1024

def allowed_file(file_name):
    return '.' in file_name and \
           file_name.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        f = request.files['fileupload']
        if f and allowed_file(f.filename):
            file_name = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
            return redirect(url_for('upload_file', filename=file_name))
    else:
        return render_template('uploadfile.html')


@app.route('/uploads/<file_name>')
def upload_file(file_name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], file_name)



if __name__ == '__main__':
    app.run()