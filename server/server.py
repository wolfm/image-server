from flask import Flask, request, jsonify
import os
from flask.helpers import send_file
from werkzeug.utils import secure_filename
from PIL import Image

VALID_EXTENSIONS = set(["jpg", "jpeg", "png", "gif", "webp"])
UPLOAD_FOLDER = 'uploads'


app = Flask(__name__, static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

photos = []

@app.before_first_request
def initPhotos():
    # For each file
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):

        # Validate extension
        if not valid_file(filename): continue

        add_photo_to_state(filename)


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':

        # Check if the post request has a file part
        if 'file' in request.files:

            return_code = 200

            # For each received file
            for file in request.files.getlist("file"):
                if file and valid_file(file.filename):

                    filename = secure_filename(file.filename)
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                    # If file exists, ignore
                    if os.path.exists(filepath): continue

                    file.save(filepath)

                    add_photo_to_state(filename)
                else:
                    return_code = 415 # Unsupported media type

            if return_code == 415:
                return "Invalid file extension", 415 # Unsupported media type
            

    return jsonify(photos), return_code


# Return json list containing photos and URLs
@app.route('/photos', methods=['GET'])
def getPhotoList():
    return jsonify(photos), 200

# Return photo data to client
@app.route('/photos/<filename>', methods=['GET'])
def getPhoto(filename):

    path = os.path.join('uploads', filename)

    if not os.path.exists(path):
        
        return f"File at '{path}' not found!", 404
    
    return send_file(path)


### HELPER FUNCTIONS ###


# Validate file against specified extensions
def valid_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in VALID_EXTENSIONS


def add_photo_to_state(filename):

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Get image properties
    img = Image.open(filepath)
    width, height = img.size

    # Update server state
    photos.append({
        'src': os.path.join('photos', filename), #TODO make photos part of config, not hardcoded
        'width': width,
        'height': height
    })
