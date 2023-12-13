#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask
import urllib.parse


app = Flask(__name__)


@app.route('/c/<path:text>')
def hello_hbnb(text):
    """replace underscore _ symbols with a space )"""
    decoded_text = urllib.parse.unquote_plus(text)
    text_notspace = decoded_text.replace('_', ' ')
    return (f'C {text_notspace}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)