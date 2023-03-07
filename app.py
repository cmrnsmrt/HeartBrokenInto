from flask import Flask, render_template, request
from flask_mysqldb import MySQL

import re

app = Flask(__name__)

# MySQL Connection Creds
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'abertaybugbounty'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/landing/')
def landing():
    return render_template('landing.html')

@app.route('/page1/')
def page1():
    return render_template('page1.html')

@app.route('/page2/')
def page2():
    return render_template('page2.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
