# 查询数据库

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='131128287', database='my01')
# conn对象可以
# rollback回滚
# commit提交修改
# close关闭

cur = conn.cursor()

sql = '''
        select * from my1 where my1.age>10;
      '''

cur.execute(sql)
# 执行 sql

# 抓取数据时，cursor会在数据上移动

result = cur.fetchall()
print(result)
print()
# 全部抓取

cur.execute(sql)
# 当完成全部抓取后，cursor在数据的最后，无法继续读取数据，需要重新执行sql重置cursor
while True:
    x = cur.fetchone()
    if not x:
        break
    print(x)
# 逐个抓取
