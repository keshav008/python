import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
if(conn.is_connected()):
    print("connection established")
    
sql= 'insert into student(name,roll,fee) values (%s,%s,%s)'
myc=conn.cursor()
params=("raju",109,45000.3)
try:
    myc.execute(sql,params)
    conn.commit()
    print("data inserted sucessfully")
except:
    conn.rollback()
    print("unable to insret data")

myc.close()
conn.close()
