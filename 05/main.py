# 超量插入

import pymysql

import random

st = 'abcdefghijklmnopqrstuvwxyz'
conn=pymysql.connect(host='localhost',port=3306,user='root',password='131128287', database='my02')
cur=conn.cursor()

for _ in range(0, 1000000):
    r=''
    for __ in range(0, 4):
        n = random.randint(0, 25)
        neo = st[n]
        r += neo
    sql='''
    insert into  my1(include) value (%s)
    '''
    cur.execute(sql,(r,))
conn.commit()