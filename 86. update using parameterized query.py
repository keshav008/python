import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
print(conn.is_connected())
sql='update student set fee=%s where fee=%s'
fe1=float(input("enter the new fees:"))
fe2=float(input("enter the prevoius fees:"))
params=(fe1,fe2)
myc=conn.cursor()
try:
    myc.execute(sql,params)
    conn.commit()
    print("table updated")
except:
    conn.rollback()
    print("unable to update table")

myc.close()
conn.close()
