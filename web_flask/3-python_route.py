#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask
import urllib.parse


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "¡Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<path:text>', strict_slashes=False)
def show_c(text):
    """replace underscore _ symbols with a space )"""
    decoded_text = urllib.parse.unquote_plus(text)
    text_notspace = decoded_text.replace('_', ' ')
    return (f'{text_notspace}')


@app.route('/python/<path:text>' strict_slashes=False)
def show_python(text):
    decoded_text = urllib.parse.unquote_plus(text)
    text_notspace = decoded_text.replace('_', ' ')
    return (f"Python {text_notspace}")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
