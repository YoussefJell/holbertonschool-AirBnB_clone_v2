#!/usr/bin/python3
"""1-hbnb_route Module"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_page():
    """Displays 'Hello HBNB!' upon visiting root page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """Displays 'HBNB' upon visiting /hbnb page"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
