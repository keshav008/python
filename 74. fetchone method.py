import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
if(conn.is_connected()):
    print("connection established sucessfully")
sql='select * from student where roll=101'
myc=conn.cursor(buffered=True)# this will read all row according to sql query and will not give unread error
try:
    myc.execute(sql)
    row=myc.fetchone()
    for r in row:
        print(r)
       # row=myc.fetchone()
    print("total rows:",myc.rowcount)
except:
    conn.rollback()
    print("unable to show")

myc.close()
conn.close()
