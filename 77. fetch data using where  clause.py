import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
if(conn.is_connected()):
    print("database connected")

sql='select * from student where name="tripti"'
myc=conn.cursor(buffered=True)
try:
    myc.execute(sql)
    row=myc.fetchone()
    print(row)

except:
    conn.rollback()
    print("unable to fetch data")
myc.close()
conn.close()
