from flask import Flask, jsonify, request
from math import sqrt
app = Flask(__name__)


@app.route("/name", methods=["GET"])
def hello():
    """
    Returns my name
    """
    data = {"name": "Chris Zhou"}
    return jsonify(data)


@app.route("/hello/<name>", methods=["GET"])
def hello_name(name):  # the name variable being passed in here is the string that the client puts in the <name> part of the url
    data = {"message": "Hello there, {}".format(name)}
    return jsonify(data)


@app.route("/distance", methods=["POST"])
def distance():
    r = request.get_json()
    a = r["a"]
    b = r["b"]
    dis = sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    data = {
        "distance": dis,
        "a": a,
        "b": b
    }
    # respond to the API caller with a JSON representation of data. jsonify is important, as it sets response headers that indicate the respose is in JSON as well
    return jsonify(data), 200
