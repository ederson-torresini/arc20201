# https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart

from flask import Flask, request
app = Flask(__name__)


@app.route("/gravar", methods=["POST"])
def gravar():
    return request.json
