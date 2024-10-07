from flask import render_template, Flask, jsonify, redirect, request
import string
from genpasswds import generate_passwords
import passwordcheck
import pwned
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
    For GET requests:
    - Expects JSON data with 'q' (quantity) and 'length' (length of each password).
    - Returns a JSON response with generated passwords or an error message if data is invalid.
    For POST requests:
    - Expects query parameters 'q' (quantity) and 'length' (length of each password).
    - Returns an HTML response with generated passwords.
    Returns:
        - JSON response with generated passwords or error message for GET requests.
        - HTML response with generated passwords for POST requests.
    """
    
   
    

    if request.method == "GET":
        q = int(request.args.get('q'))
        length = int(request.args.get('length'))
        passwds = gen_list(q, length)
        return render_template('success.html', liste=passwds)
    else:
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
    
@ app.route("/breach")
def breach_check():
    return render_template("pwnd.html")

@app.route("/pwnd", methods=["POST", "GET"])
def pwnd():
    if request.method == "POST":
        password = str(request.form['pw'])
        pw = pwned.password(password)
        if pw == False:
            return render_template("safe.html", data=password)
        else:
            return render_template("compromised.html", data=password)

@ app.route("/strength")
def strength_check():
    return render_template("password_check_form.html")

@ app.route("/strength/check", methods=["POST", "GET"])
def check():
    """
    Check the strength of a password.
    Returns: the strength of the password
    Get and Post requests are supported.
    """
    if request.method == "POST":
        password = request.form.get('pw')
        strength, reasons = passwordcheck.check_password(password)
        pw = pwned.password(password)
        return render_template("password_result.html", strength=strength, reasons=reasons, password=password, pwned=pw)
    else:
        password = request.form.get('pw')
        strength, reasons = passwordcheck.check_password(password)
        return strength

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

    #Todo: Add a new route that will check if the password is strong or weak
    #Research: How to check if a password is strong or weak
    #Todo: Add a new route that will check if the password is in the list of the most common passwords
    #Research: How to check if a password is in the list of the most common passwords
    #Todo : Add a new route that will check if that password has been pwned
    #Research: How to check if a password has been pwned any api that can be used to check if a password has been pwned?

    #Todo: Add a  system that will allow users to create a local Sqlite Database and store their passwords locally
    #Research: How to create a local Sqlite Database and store passwords locally