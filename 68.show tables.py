import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost',)
if(conn.is_connected()):
    print('connected to database python')
sql='show tables'
myc=conn.cursor()
myc.execute(sql)
for tbl in myc:
    print(tbl)

myc.close()
conn.close()
