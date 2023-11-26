import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost',)
if(conn.is_connected()):
    print('connected to database python')

sql='insert into student(name,roll,fee) values("prashant",101,50000.5)'
#val=("prashant",102,70000.5)
myc=conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print("data inserted sucessfully")
except:
    conn.rollback()
    print("unable to insert data")

myc.close()
conn.close()
