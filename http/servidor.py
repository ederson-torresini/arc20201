# Obtido de https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
