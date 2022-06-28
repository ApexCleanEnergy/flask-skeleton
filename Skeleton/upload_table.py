from flask import Flask, render_template, request, redirect
import os
import csv



app = Flask(__name__)
app.config['FILE_UPLOADS'] = r"Skeleton\static\file\uploads"
app.config["DEBUG"] = True


@app.route('/')
def index():
    return render_template('index_upload_data.html')

@app.route('/', methods=["GET", "POST"])
def upload_data():
    if request.method == 'POST':
        if request.files:
            uploaded_file = request.files['filename']
            filepath = os.path.join(app.config['FILE_UPLOADS'], uploaded_file.filename)
            uploaded_file.save(filepath)
    return render_template('index_upload_success.html')

if (__name__ == "__main__"):
     app.run(port = 5000)