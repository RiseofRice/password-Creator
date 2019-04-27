from flask import render_template, Flask, jsonify, redirect, request
import string
from genpasswds import generate_passwords


app = Flask(__name__)




@app.route("/")
def helloworld():
    return render_template("index.html")
# app.config["Ser"]

@app.route('/new', methods=["GET", "POST"])
def input():

    if request.method == "POST":
        q = int(request.form['q'])
        length = int(request.form['length'])
        passwds = generate_passwords(q, length)
        return render_template('success.html', liste=passwds)
               
        
        
    else:
        
        q = int(request.args.get('q'))
        length = int(request.args.get('length'))
        passwds = generate_passwords(q, length)
        return render_template('success.html', liste=passwds)
        



        
    




