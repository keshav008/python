import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
print(conn.is_connected())
sql='delete from student where stuid=%s'
myc=conn.cursor()
stid=int(input("enter student id wants to delete:"))
del_value=(stid,)# coverting to tuple tup[e
try:
    myc.execute(sql,del_value)
    conn.commit()
    print("data deleted")
except:
    conn.rollback()
    print("unable to delete data")

myc.close()
conn.close()
