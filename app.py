from flask import Flask, request, send_from_directory, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    files = sorted(os.listdir(app.config['UPLOAD_FOLDER']), key=lambda x: os.path.getctime(os.path.join(app.config['UPLOAD_FOLDER'], x)), reverse=False)
    return render_template('index.html', files=files)


@app.route('/preview/<filename>')
def preview_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    files = request.files.getlist('file')  # Get a list of uploaded files

    uploaded_files = []

    for file in files:
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uploaded_files.append(filename)

    if uploaded_files:
        return "Files uploaded successfully: " + ', '.join(uploaded_files)
    else:
        return "No files uploaded"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
