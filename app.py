from flask import Flask
from flask import render_template

import os
import socket

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello!"


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=9090)
