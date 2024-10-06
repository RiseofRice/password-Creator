from flask import render_template, Flask, jsonify, redirect, request
import string
from genpasswds import generate_passwords

from genlist import gen_list
import os
import requests
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


@ app.route("/")
def helloworld():
    """
    Renders the index.html template.
    Returns:
        Response: The rendered HTML template for the index page.
    """

    return render_template("index.html")


@ app.route('/new', methods=["GET", "POST"])
def new():
    """
    Handle the creation of new passwords based on the request method.
    For POST requests:
    - Expects a JSON payload with 'q' (quantity) and 'length' (length of each password).
    - Validates the presence and validity of 'q' and 'length'.
    - Generates a list of passwords and returns them in JSON format.
    For GET requests:
    - Expects 'q' and 'length' as query parameters.
    - Generates a list of passwords and renders them in an HTML template.
    Returns:
        - JSON response with generated passwords for POST requests.
        - Rendered HTML template with generated passwords for GET requests.
        - JSON error response with appropriate status code for invalid data.
    """
   
    

    if request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        q = data.get('q')
        length = data.get('length')
        if not q or not length:
            return jsonify({"error": "Invalid data provided"}), 400
        
        q = int(q)
        length = int(length)
        if q < 1 or length < 1:
            return jsonify({"error": "Invalid data provided"}), 400
        
        passwds = gen_list(q, length)
        return jsonify({"passwords": passwds})
    else:
        q = int(request.args.get('q'))
        length = int(request.args.get('length'))
        passwds = gen_list(q, length)
        return render_template('success.html', liste=passwds)


@ app.route("/1pass", methods=["POST", "GET"])
def onePass():
    """
    Generates a single password.
    Returns: the password
    Get and Post requests are supported.
    """
    if request.method != "POST":
        password = generate_passwords(length=25)
        return password
    else:
        password = generate_passwords(length=25)
        return password

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)