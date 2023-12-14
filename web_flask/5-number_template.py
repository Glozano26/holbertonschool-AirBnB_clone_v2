#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask
from flask import render_template
import urllib.parse


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    """replace underscore _ symbols with a space )"""
    decoded_text = urllib.parse.unquote_plus(text)
    text_notspace = decoded_text.replace('_', ' ')
    return (f'C {text_notspace}')


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def show_python(text="is cool"):
    decoded_text = urllib.parse.unquote_plus(text)
    text_notspace = decoded_text.replace('_', ' ')
    return (f"Python {text_notspace}")


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_H1(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
