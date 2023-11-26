import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
if(conn.is_connected()):
    print('connection established sucessfully')
sql='update student set name="tripti" where stuid=1'
myc=conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print("table updated sucessfully")
except:
    conn.rollback()
    print("unable to update table")

myc.close()
conn.close()
