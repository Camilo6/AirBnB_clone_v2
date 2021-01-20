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


@app.route("/c/<string:text>", methods=["GET"], strict_slashes=False)
def croute(text):
    """return C ..."""
    return 'C {}'.format(text.replace("_", " "))

@app.route("/python", defaults={"text": "is cool"}, methods=["GET"],
           strict_slashes=False)
@app.route("/python/<string:text>", methods=["GET"], strict_slashes=False)
def pythonroute(text):
    """return C ..."""
    return 'Python {}'.format(text.replace("_", " "))



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
