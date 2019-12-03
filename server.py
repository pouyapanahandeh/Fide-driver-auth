#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
from flask import Flask,render_template
from flask import request
from flask_sqlalchemy import sqlalchemy
import sys
import traceback
import pymysql
from PIL import Image
import os
# __name__  这里的下划线是两个 —— ——
app = Flask(__name__)


# index page
@app.route('/',methods=['GET','POST'])
def login():
    return render_template('login.html')

def my_sql(sql):
    #connect to database
    conn=pymysql.connect(host='localhost',user='root',password='ruirui123',db='image',port=3306,
           charset='utf8',autocommit=True)#autocommit sql
    cur=conn.cursor(pymysql.cursors.DictCursor)#set cursor,return dict
    cur.execute(sql)#execute sql
    res=cur.fetchone()#return one data
    cur.close()#close cursor
    conn.close()#close database
    return res

# login request
@app.route('/login/<number>',methods=['GET','POST'])

def convert2bin(image):
    fp = open(image, 'rb')
    img = fp.read()
    return img

def login_post(number):
    if number == "1":
        username = request.form['email']
        password = request.form['password']
        num = 0
        # tu = sql.select("select * from user_info where user_name='" + username + "' and user_password='" + password + "';")
        tu = my_sql("select * from user_info where username='" + username + "' and password='" + password + "';")
        print(tu)
        for data in tu:
            num = num + 1
        if (num != 0):
            return render_template('index.html')
            my_sql.close()
        else:
            return render_template('register.html')
            my_sql.close()
    if number == "2":
        return render_template('reset-password.html')
    elif number == "3":
        return render_template('register.html')
    else:
        return render_template('error-500.html')


@app.route('/register/', methods=['GET'])
def register1():
    return render_template('register.html')

# register request
@app.route('/registerAction', methods=['POST'])
def register():
    #
    username = request.form['email']
    password = request.form['password']
    image = request.files['img']
    data = image.read()
    database = pymysql.connect(host="localhost", user="root", passwd="ruirui123", db="image")
    cursor = database.cursor()
    sql_insert = ' INSERT INTO user_info(username,password,image) VALUE ("%s","%s","%s");'
    args = (username,password,data)
    cursor.execute(sql_insert, args)
    database.commit()
    cursor.close()
    database.close()
    return render_template('login.html')

@app.route('/upload', methods=['GET'])
def upload():
    return render_template('upload.html')

@app.route('/uploadPic',methods=['POST'])
def uploadPic():
    image = request.form['imagefile1']
    sql_insert = ' INSERT INTO imagefiles(id_photo) VALUE ("%s");'%(image)
    try:
        my_sql(sql_insert)
        return render_template('upload.html')
    except:
        traceback.print_exc()
        my_sql.rollback()
        return 'register failed'
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)