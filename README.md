<h1 style="text-align:center;">~~~Flask Password Generator~~~</h1>

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)
____

## Installation 

#### Dependencies

You'll need Python 3.11 and Flask installed </br>
Flask 
___
just install the Requirements.txt with the command </br>
`pip install -r requirements.txt` maybe with sudo in unix systems </br>
and run it with `python app.py`
___

you can use the dockerfile too:

 - `docker build -t FlaskPasswords:latest .` in the root folder of this script

After that:

 - `docker run --name Flask-App -d -p 8080:8080 FlaskPasswords`

Or use docker-compose:

 - `docker-compose up -d --build`

Maybe the rendered html needs to be adapted to your port configuration especially the redirect action in the form 
____
Usage
-
after the installation it's available on `0.0.0.0:8080 which means 127.0.0.1:8080` on Docker</br>
and `0.0.0.0:8080` on native Python 
___

On the website are just 2 Input Boxes. </br>

 - The First one are the quantity of Passwords you want to generate
 - The Second one are the length of your generated Passwords

 Note: <b>The complexity is a standard and isn't adjustable</b>
___
You can also send a GET Request to the Webapp

for example `0.0.0.0:8080/new?q=8&length=25` </br>
___
License  [![](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) :scroll:
-
