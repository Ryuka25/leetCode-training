#!/usr/env/ python

from flask import *
from flask.json import dump, dumps
from werkzeug.utils import HTMLBuilder

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/table/<number>')
def table(number):
    number = int(number)
    html = ""
    for i in range(0,10):
        html += f"{number} * {i} = {number*i} <br>"
    
    return html

@app.route('/postvar')
def postvar():
    return dumps(request.form())

@app.route('/loginAction')
def login():

    def checkMatch(userLogin, userPassword):
        result = False
        if (userLogin == "test"):
            if (userPassword == "test"):
                result = True

        return result

    userLogin = request.form('userLogin')
    userPassword = request.form('userPassword')
    if (checkMatch(userLogin, userPassword)):
        page = render_template('home.html')
    else:
        page = render_template('login.html')

    return f"{userLogin}, {userPassword}"

if __name__ == '__main__':
    app.run(debug= True)
