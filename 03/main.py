# SQL注入

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='131128287', database='my01')

cur = conn.cursor()

name=input('target')
id=int(input('id'))

#  正常来说，只有把id name匹配才能显示对应对象
#  在name中输入      ' or 1=1; #       试试


sql = '''
        select * from my1 where name ='%s' and id=%d;
      '''%(name , id)

cur.execute(sql)

while True:
    x = cur.fetchone()
    if not x:
        break
    print(x)

#  实际上执行的是
#  select * from my1 where     name =''  or 1=1
#  and id=%d;被我们输入的 # 注释掉了
