#! /usr/bin/env python
# -*- coding: utf-8 -*-


import mysql.connector

class MySQL(object):
    def __init__(self,host = 'localhost', port='3306',username='root',password='Feng950814', db='smartexpense',charest='utf-8'):
    # def __init__(self, host='localhost', port='3306', username='root', password='Feng950814', db='smartexpense'):
        self.host = host
        self.port = port
        self.user = username
        self.password = password
        self.db = db
        self.charest = charest

    def connection(self):
        conn = mysql.connector.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.db)

        return conn

    def select(self,sql):
        conn = self.connection()
        cursor = conn.cursor()

        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except Exception as e:
            raise e
        finally:
            cursor.close()
            conn.close()
