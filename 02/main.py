# 操作

import pymysql

conn=pymysql.connect(host='localhost',port=3306,user='root',password='131128287',database='my01')
cur=conn.cursor()
sql='''
INSERT INTO my1(name,age,birthday,slogon,abandon,gender,type) VALUES ('安倍晋三',67,'2021-3-22','peace',1,'male',8)
'''
cur.execute(sql)
conn.commit()