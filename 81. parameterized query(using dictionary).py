import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
print(conn.is_connected())
sql='insert into student (name,roll,fee) values(%(name)s,%(roll)s,%(fee)s)'
myc=conn.cursor()
try:
    myc.execute(sql,{'name':'kajal','roll':115,'fee':54000})
    conn.commit()
    print("data inserted")
except:
    conn.rollback()
    print("unable to insert data")

myc.close()
conn.close()
    
