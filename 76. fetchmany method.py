import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
if(conn.is_connected()):
    print("connected")

sql='select * from student where roll=101'
myc=conn.cursor(buffered=True)
try:
    myc.execute(sql)
    row=myc.fetchmany(2)
    for r in row:
        print(r)
    print("total rows:",myc.rowcount)
except:
    conn.rollback()
    print("unable to show")
myc.close()
conn.close()
