from flask import Flask, render_template, request
from flask_mysqldb import MySQL

import re

app = Flask(__name__, static_folder="/Users/cameronsmart/Documents/GitHub/HeartBrokenInto/static", template_folder="/Users/cameronsmart/Documents/GitHub/HeartBrokenInto/templates")

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/landing/')
def landing():
    return render_template('landing.html')

@app.route('/game/')
def page1():
    return render_template('game.html')

@app.route('/page2/')
def page2():
    return render_template('page2.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
