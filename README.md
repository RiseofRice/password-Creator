<h1 style="text-align:center;">~~~Flask Password Generator~~~</h1>

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)
____

## Installation 

#### Dependencies

You'll need Python 3.6 and Flask installed </br>
Flask 
___
just install the Requirements.txt with the command </br>
`pip install -r requirements.txt` maybe with sudo in unix systems </br>
and run it with `python app.py`
___

you can use the dockerfile too:

 - `docker build -t FlaskPasswords:latest .` in the root folder of this script

After that:

 - `docker run --name Flask-App -d -p 8000:5000 FlaskPasswords`
____
Usage
-
after the installation it's availeble on `0.0.0.0:8000` on Docker</br>
and '0.0.0.0:5000' on native Python 
___

Website are just 2 Input Boxes. </br>

 - The First one are the quantity of Passwords
 - The Second one are the length of the Passwords

 Note: the complexity is a standard an not adjustable
___
You can also send a GET Request to the Webapp

for example `0.0.0.0:8000/new?q=8&length=25` </br>
___
License  [![](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) :scroll:
-