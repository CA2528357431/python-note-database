# 反SQL注入

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='131128287', database='my01')

cur = conn.cursor()

name = input('target')
tarid = input('id')
params=(name,tarid)

sql = '''
        select * from my1 where name =%s and id=%s;
      '''
# 注意，%s没有''，python会自动匹配


cur.execute(sql, params)

while True:
    x = cur.fetchone()
    if not x:
        break
    print(x)
