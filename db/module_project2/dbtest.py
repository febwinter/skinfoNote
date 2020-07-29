'''
1. db module 로드 (mysql)
2. db connection (url, user, pw, dbname)
3. execute query (DML - SLECT, INSERT, UPDATE, DELETE)
    - sql 작성 (str)
    - sql 실행 (execute 사용)
    - select 
'''

import pymysql
from prettytable import PrettyTable

conn = pymysql.connect(host='127.0.0.1',
                port=3306,
                user='root',
                password='password',
                db='repl_db',
                charset='utf8')

curs = conn.cursor()
# print(curs)

# insertSql = 'insert into member(name) values(%s)'
# curs.execute(insertSql, ('HHH'))
# conn.commit()

rows = curs.execute('select * from member')
selectSql = 'select * from member where name like %s'
t = PrettyTable(['id','name'])
col = []
for col_object in curs.description:
    col.append(col_object[0])

print(col)


#for row in curs.fetchall():
#    #print(row)
#    t.add_row(row)

print(t)

