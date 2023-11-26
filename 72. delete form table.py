import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
if (conn.is_connected()):
    print("connected to database")
print()
print("table before insertion")
sql='select * from student'
myc=conn.cursor()
myc.execute(sql)
for data in myc:
    print(data)
sql1='delete from student where roll=105'
myc.execute(sql1)
print('table after deleting')
sql2='select * from student'
myc.execute(sql2)
for data in myc:
    print(data)
myc.close()
conn.close()
