from flask import Flask, request, flash, redirect, url_for
import pathlib, os
from werkzeug.utils import secure_filename

VALID_EXTENSIONS = set(["jpg", "jpeg", "png", "gif"])
UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def serve_index():
    return "Hello World!"

@app.route('/upload', methods=['get', 'POST'])
def upload():
    if request.method == 'POST':
        # Check if the post request has a file part
        if 'file' not in request.files:
            # flash("No file found")
            print("No file found")
            return redirect('/')

        file = request.files['file']

        if file.filename == '':
            # flash('No selected file')
            print("No selected file")
            return redirect('/')

        print("File found")

        if file and valid_extension(file.filename):
            print("Valid filename!")
            filename = secure_filename(file.filename)
            print("Secure filename:", filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            print("Invalid extension")

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
        
def valid_extension(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in VALID_EXTENSIONS
