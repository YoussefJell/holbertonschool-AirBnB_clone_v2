#!/usr/bin/env python3
"""4-number_route Module"""
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


@app.route('/c/<text>', strict_slashes=False)
def C_page(text):
    """Displays 'C (text variable with spaces instead of _'s)'
        upon visiting /c/<text> page
        (text is optional)"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_page(text="is cool"):
    """Displays 'Python (text variable with spaces instead of _'s)'
        upon visiting /python/<text> page
        (text default = "is cool")"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_page(n):
    """Displays '(Variable n) is a number'
        upon visiting /number/(number) page
        if n is really a number."""
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host="0.0.0.0")