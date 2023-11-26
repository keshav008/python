import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
if(conn.is_connected):
    print("conected to database sucessfully")
sql='insert into student(name,roll,fee) values("sumit",103,5000),("harman",105,700)'
myc=conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print("data inserted sucessfully")
except:
    conn.rollback()
    print("unable to insert data")

print("inserted data")
sql2='select * from student'
myc.execute(sql2)
for data in myc:
    print(data)
myc.close()
conn.close()
