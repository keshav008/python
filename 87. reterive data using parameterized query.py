import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
print(conn.is_connected())
sql='select * from student where stuid=%s'
myc=conn.cursor()
sid=int(input("enter the id of student whose data is needed:"))
params=(sid,)
try:
    myc.execute(sql,params)
    row=myc.fetchone()
    print(row)
except:
    conn.rollback()
    print("unable to fetch data:")

myc.close()
conn.close()
