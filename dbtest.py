import pymysql
conn = pymysql.connect("localhost","root","123456","cowcat")
cursor = conn.cursor()
cursor.execute('select * from users')
values = cursor.fetchall()
print(values)
conn.close()
