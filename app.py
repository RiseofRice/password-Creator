from flask import render_template, Flask, jsonify, redirect, request
import string
from genpasswds import generate_passwords
import sha1
from genlist import gen_list
import os
import requests
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


@ app.route("/")
def helloworld():
    return render_template("index.html")


@ app.route('/new', methods=["GET", "POST"])
def new():

    if request.method == "POST":
        q = int(request.form['q'])
        length = int(request.form['length'])
        passwds = gen_list(q, length)
        return render_template('success.html', liste=passwds)
    else:
        q = int(request.args.get('q'))
        length = int(request.args.get('length'))
        passwds = gen_list(q, length)
        return render_template('success.html', liste=passwds)


@ app.route("/1pass", methods=["POST", "GET"])
def onePass():
    if request.method != "POST":
        password = generate_passwords(length=25)
        return password
    else:
        password = generate_passwords(length=25)
        return password

# TODO Register key funtion schreiben


@ app.route("/registerkey")
def registerkey():
    return render_template("register_key.html")


@ app.route("/registered", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        q = request.args.get('key')
        print(q)
        element = {"API_KEY": q}
        with open("apikey.json", "w") as jsonfile:
            json.dump(element, jsonfile)
        return "<h1> Saved </h1>"
    else:
        return render_template("404.html")


@ app.route('/checkmy/<password>', methods=["POST", "GET"])
def shouldnotbeused(password):
    if sha1.check(password) == True:
        return render_template("compromised.html", data=f"'{password}'")
    else:
        return "<h1>you're safe</h1>"


@ app.route('/api/check', methods=["POST", "GET"])
def apicheck():
    if request.method == "POST":

        dictionary = request.args.to_dict()
        keys = []
        for key in dictionary:
            keys.append(key)
        print(keys)
        if keys[0] == "password":
            if sha1.check(dictionary["password"]) == True:
                return f"{dictionary['password']} is compromied"
            else:
                return "youre safe"
        # else:
        #     return "something went wrong"
    # if sha1.check(password) == True:
    #     return "<h1> you got compromised</h1>"
    # else:
    #     return "<h1>you're safe</h1>"


if __name__ == "__main__":

    app.run(host='127.0.0.1', port=8080, debug=True)
