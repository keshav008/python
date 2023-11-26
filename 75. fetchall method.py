import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
if(conn.is_connected()):
    print("connection established sucesfully")
else:
    print("database not connected")
    
sql='select * from student where roll=101'
myc=conn.cursor()
try:
    myc.execute(sql)
    row=myc.fetchall()
    for r in row:
        print(r)
    print("total row:",myc.rowcount)
except:
    conn.rollback()
    print("unable to show")

myc.close()
conn.close()
