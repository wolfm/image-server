from flask import Flask, request, redirect, render_template, url_for
import pathlib, os
from flask.templating import render_template
from werkzeug.utils import secure_filename

VALID_EXTENSIONS = set(["jpg", "jpeg", "png", "gif"])
UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Check if the post request has a file part
        if 'file' not in request.files:
            # flash("No file found")
            print("No file found")
            return render_template("index.html")

        for file in request.files.getlist("file"):
            if file and valid_file(file.filename):
                print("Valid filename!")
                filename = secure_filename(file.filename)
                print("Secure filename:", filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                print("Invalid extension")

    return render_template("index.html")
        
def valid_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in VALID_EXTENSIONS
