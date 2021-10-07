from flask import Flask, request, redirect
import os
from flask.helpers import send_file
from werkzeug.utils import secure_filename

VALID_EXTENSIONS = set(["jpg", "jpeg", "png", "gif"])
UPLOAD_FOLDER = 'uploads'

app = Flask(__name__, static_url_path='', static_folder='../client/build')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['POST'])
def upload():
    if request.method == 'POST':

        # Check if the post request has a file part
        if 'file'  in request.files:

            # For each received file
            for file in request.files.getlist("file"):
                if file and valid_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                else:
                    return "Invalid file extension", 415 # Unsupported media type

    return redirect(request.url)


# Return json list containing photos and URLs
# @app.route('/photos', methods=['GET'])
# def getPhotoList():
#     pass

# Return photo data to client
@app.route('/photos/<filename>', methods=['GET'])
def getPhoto(filename):

    path = os.path.join('uploads', filename)

    if not os.path.exists(path):
        
        return f"File at '{path}' not found!", 404
    
    return send_file(path)
        
def valid_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in VALID_EXTENSIONS
