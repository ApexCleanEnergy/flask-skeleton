"""
Routes and views for the flask application.
"""

from Skeleton import app
from flask import request, render_template

@app.route('/')
def home_page():
    return render_template(
        "file_complaint.html",
        test_param="blake bailes",
    )

@app.route('/filed_complaint.php', methods=['GET'])
def submission_page():
    R = request.args #request.form #for post requests
    return R