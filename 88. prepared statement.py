import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
print(conn.is_connected())
sql='insert into student (name,roll,fee) values (?,?,?)'
myc=conn.cursor(prepared=True)
try:
    myc.execute(sql,("ryan",121,20000))
    conn.commit()
    print("data inserted")
except:
    conn.rollback()
    print("unable to insert data in table")

myc.close()
conn.close()

    
