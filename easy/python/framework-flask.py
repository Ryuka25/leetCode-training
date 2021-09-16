#!/usr/env/ python

from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return "my first website"

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=500, debug= True)
