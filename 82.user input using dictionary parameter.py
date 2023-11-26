import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
print(conn.is_connected())
sql='insert into student(name,roll,fee) values (%(name)s,%(roll)s,%(fee)s)'
myc=conn.cursor()
nm=input("enter name:")
rl=int(input("enter roll:"))
fe=float(input("enter fees:"))
params={'name':nm,'roll':rl,'fee':fe}
try:
    myc.execute(sql,params)
    conn.commit()
    print("data inserted")
except:
    conn.rollback()
    print("unable to insert data")

myc.close()
conn.close()
