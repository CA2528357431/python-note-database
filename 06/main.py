# 从数据库中获取信息

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='131128287', database='my01')
sql='''
select * from my1 left join my2 on my1.id=my2.id;
'''
cur = conn.cursor()
cur.execute(sql)
data = cur.fetchall()
for x in data:
    for y in x:
        st = str(y)
        stt = st.ljust(13,' ')
        print(stt, end=' ')
    print()