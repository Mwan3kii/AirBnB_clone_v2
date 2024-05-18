#!/usr/bin/python3
"""Starts a Flask web application listening on 0.0.0.0 port 5000"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays hello hbnb on route /"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB on route /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display string c then text var replacing _ with space"""
    return "C " + str(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Displays python then text var replacing _ with space"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num_n(n):
    """Display if n is an interger"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_n(n):
    """Displays html page if n is interger"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
