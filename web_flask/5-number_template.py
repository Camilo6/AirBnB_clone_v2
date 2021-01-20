#!/usr/bin/python3
""" HBNB """


from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def hello():
    """return hello HBNB"""
    return 'Hello HBNB!'


@app.route("/hbnb", methods=["GET"], strict_slashes=False)
def hbn():
    """return HBNB"""
    return 'HBNB'


@app.route("/c/<string:text>", methods=["GET"], strict_slashes=False)
def croute(text):
    """return C ..."""
    return 'C {}'.format(text.replace("_", " "))


@app.route("/python", defaults={"text": "is cool"}, methods=["GET"],
           strict_slashes=False)
@app.route("/python/<string:text>", methods=["GET"], strict_slashes=False)
def pythonroute(text):
    """return Python ..."""
    return 'Python {}'.format(text.replace("_", " "))


@app.route("/number/<int:n>", methods=["GET"], strict_slashes=False)
def number(n):
    """return a integer"""
    return '%d is a number' % n


@app.route("/number_template/<int:n>", methods=["GET"], strict_slashes=False)
def number_template(n):
    """return a template"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
