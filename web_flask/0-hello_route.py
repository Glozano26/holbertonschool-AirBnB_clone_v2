#!/usr/bin/python3
'''
MODULE NAME:
------------
    0-hello_route

MODULE DESCRIPTION:
-------------------
    That starts a Flask web application

MODULE ATTRIBUTES:
------------------
    None
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    
    return ("¡Hola HBNB!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
