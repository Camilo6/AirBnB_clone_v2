#!/usr/bin/python3
""" HBNB """


from flask import Flask
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def hello():
    """return hello HBNB"""
    return 'Hello HBNB!'


@app.route("/hbnb", methods=["GET"], strict_slashes=False)
def hbn():
    """return HBNB"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
