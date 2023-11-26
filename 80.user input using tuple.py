import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
print(conn.is_connected())
sql='insert into student (name,roll,fee) values (%s,%s,%s)'
myc=conn.cursor()
nm=input("enter name:")
rl=int(input("enter roll no:"))
fe=float(input("enter fees:"))
params=(nm,rl,fe)
try:
    myc.execute(sql,params)
    conn.commit()
    print("data inserted")
except:
    conn.rollback()
    print("unable to insert")
myc.close()
conn.close()
