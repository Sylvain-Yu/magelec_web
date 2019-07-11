# -*- coding: utf-8 -*-
# @Author: sylvain
# @Date:   2019-07-09 13:03:23
# @Last Modified by:   sylvain
# @Last Modified time: 2019-07-09 13:25:29
import mysqlclient.MySQLdb

db = MySQLdb.connect('127.0.0.1','testuser','test123','testdb')

cursor = db.cursor()

cursor.execute('DROP TABLE IF EXIST EMPLOYEE')

sql = '''CREATE TABLE EMPLOYEE(
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    )
    '''

cursor.execute(sql)

cursor.close()
db.close()