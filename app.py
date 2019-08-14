from flask import render_template, Flask, jsonify, redirect, request
import string
from genpasswds import generate_passwords
import sha1
from genlist import gen_list

app = Flask(__name__)




@app.route("/")
def helloworld():
    return render_template("index.html")
# app.config["Ser"]

@app.route('/new', methods=["GET", "POST"])
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

@app.route('/checkmypw/<password>')
def shouldnotbeused(password):
    if sha1.check(password) == True:
        return "<h1> you got compromised</h1>"
    else:
        return "<h1>you're safe</h1>"





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
        



        
    




