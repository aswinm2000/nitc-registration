import os,json,requests,csv,datetime
from sqlathanor import FlaskBaseModel, initialize_flask_sqlathanor,declarative_base, Column, relationship, AttributeConfiguration
from flask_bcrypt import Bcrypt
from flask import Flask, render_template, url_for, flash, redirect, jsonify, flash, request, session, send_file
from datetime import datetime
from datetime import date
import time
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from sqlalchemy import Integer, String,create_engine,exc
from sqlalchemy.types import Integer,Text,String, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
import pandas as pd
from functools import wraps
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import traceback
from db import *
import credentials

BaseModel = declarative_base()
app = Flask(__name__)
app.secret_key = 'asfasfasdasdasda'
CORS(app)

USERNAME = credentials.Username
PASSWORD = credentials.Password
DB_NAME = credentials.Database
HOST= credentials.Host

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'+USERNAME+':'+PASSWORD+'@'+HOST+'/'+DB_NAME

engine = create_engine('postgresql+psycopg2://'+USERNAME+':'+PASSWORD+'@'+HOST+'/'+DB_NAME)

db.app = app
db.init_app(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)

@hybrid_property
def hybrid(self):
    return self._hybrid

@hybrid.setter
def hybrid(self, value):
    self._hybrid = value

@hybrid.expression
def hybrid(cls):
    return False

@app.route('/login')
def login():
    session.clear()
    return render_template('Login.html')


@app.route('/authenticate', methods=['GET','POST'])
def authenticate():
    if request.method== 'POST':
        username = request.form('username')
        password = request.form('password')
        print("User authenticated")
        return (redirect(url_for('view')))
    elif sentdata.status_code == 401:
        flash("Wrong password")

    else:
        print()

    return render_template('Register.html', title='Register', form=form)



if (__name__ =="__main__"):
    app.debug=True
    app.run(port='8081')
