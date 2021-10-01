from flask import Flask, request, redirect, render_template, url_for
import pathlib, os
from flask.helpers import send_from_directory, send_file
from flask.templating import render_template
from werkzeug.utils import secure_filename

VALID_EXTENSIONS = set(["jpg", "jpeg", "png", "gif"])
UPLOAD_FOLDER = 'uploads'

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Check if the post request has a file part
        if 'file' not in request.files:
            # flash("No file found")
            print("No file found")
            return send_from_directory(app.static_folder, 'index.html')

        for file in request.files.getlist("file"):
            if file and valid_file(file.filename):
                print("Valid filename!")
                filename = secure_filename(file.filename)
                print("Secure filename:", filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                print("Invalid extension")

    return send_from_directory(app.static_folder, 'index.html')

# Return json list containing photos and URLs
# @app.route('/photos', methods=['GET'])
# def getPhotoList():
#     pass

# Return photo data to client
@app.route('/photos/<filename>', methods=['GET'])
def getPhoto(filename):

    path = os.path.join('uploads', filename)

    if not os.path.exists(path):
        print("File not found!")
        return 404
    
    return send_file(path)
        
def valid_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in VALID_EXTENSIONS
