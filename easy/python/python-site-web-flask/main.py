#!/usr/env/ python

from flask import *
from models.User import *

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

@app.route('/loginAction', methods=['POST'])
def login():

    inputUsername = request.form['userLogin']
    inputPassword = request.form['userPassword']
    if (User.checkMatch(inputUsername, inputPassword)):
        user = User.getUserByUsername(inputUsername);
        page = {
            'title':'Homepage'
        }
        html = render_template('home.html', user = user, page = page)
    else:
        html = render_template('loginError.html')

    return html;

if __name__ == '__main__':
    app.run(debug= True)
