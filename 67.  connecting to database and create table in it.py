import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost',)
if(conn.is_connected()):
    print('connected to database python')

sql='create table student(stuid int auto_increment primary key, name varchar(20),roll int, fee float)'
myc=conn.cursor()
myc.execute(sql)
myc.close()
conn.close()
