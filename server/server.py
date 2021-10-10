from flask import Flask, request, jsonify, redirect
import os
from flask.helpers import send_file
from werkzeug.utils import secure_filename
from PIL import Image

VALID_EXTENSIONS = set(["jpg", "jpeg", "png", "gif", "webp"])
UPLOAD_FOLDER = 'uploads'

app = Flask(__name__, static_url_path='', static_folder='../client/build')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':

        # Check if the post request has a file part
        if 'file' in request.files:

            # For each received file
            for file in request.files.getlist("file"):
                if file and valid_file(file.filename):

                    # Save file
                    filename = secure_filename(file.filename)
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(filepath)

                    # Get image properties
                    img = Image.open(filepath)
                    width, height = img.size

                    # Update server state
                    photos.append({
                        'src': os.path.join('photos', filename), #TODO make photos part of config, not hardcoded
                        'width': width, # TODO calculate
                        'height': height
                    })
                else:
                    return "Invalid file extension", 415 # Unsupported media type

    return jsonify(photos), 200


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
        
def valid_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in VALID_EXTENSIONS

photos = []
#     {
#       'src': "http://localhost:5000/photos/grapes.jpg",
#       'width': 4,
#       'height': 3
#     },
#     {
#       'src': "http://localhost:5000/photos/abstract_crop.jpg",
#       'width': 1,
#       'height': 1
#     },
#     {
#       'src': "https://source.unsplash.com/Dm-qxdynoEc/800x799",
#       'width': 1,
#       'height': 1
#     },
#     {
#       'src': "https://source.unsplash.com/qDkso9nvCg0/600x799",
#       'width': 3,
#       'height': 4
#     },
#     {
#       'src': "https://source.unsplash.com/iecJiKe_RNg/600x799",
#       'width': 3,
#       'height': 4
#     },
#     {
#       'src': "https://source.unsplash.com/epcsn8Ed8kY/600x799",
#       'width': 3,
#       'height': 4
#     },
#     {
#       'src': "https://source.unsplash.com/NQSWvyVRIJk/800x599",
#       'width': 4,
#       'height': 3
#     },
#     {
#       'src': "https://source.unsplash.com/zh7GEuORbUw/600x799",
#       'width': 3,
#       'height': 4
#     },
#     {
#       'src': "https://source.unsplash.com/PpOHJezOalU/800x599",
#       'width': 4,
#       'height': 3
#     },
#     {
#       'src': "https://source.unsplash.com/I1ASdgphUH4/800x599",
#       'width': 4,
#       'height': 3
#     },
#     {
#       'src': "https://source.unsplash.com/XiDA78wAZVw/600x799",
#       'width': 3,
#       'height': 4
#     },
#     {
#       'src': "https://source.unsplash.com/x8xJpClTvR0/800x599",
#       'width': 4,
#       'height': 3
#     },
#     {
#       'src': "https://source.unsplash.com/u9cG4cuJ6bU/4927x1000",
#       'width': 4927,
#       'height': 1000
#     },
#     {
#       'src': "https://source.unsplash.com/qGQNmBE7mYw/800x599",
#       'width': 4,
#       'height': 3
#     },
#     {
#       'src': "https://source.unsplash.com/NuO6iTBkHxE/800x599",
#       'width': 4,
#       'height': 3
#     },
#     {
#       'src': "https://source.unsplash.com/pF1ug8ysTtY/600x400",
#       'width': 4,
#       'height': 3
#     },
#     {
#       'src': "https://source.unsplash.com/A-fubu9QJxE/800x533",
#       'width': 4,
#       'height': 3
#     },
#     {
#       'src': "https://source.unsplash.com/5P91SF0zNsI/740x494",
#       'width': 4,
#       'height': 3
#     }
#   ]