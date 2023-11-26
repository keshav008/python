import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',host='localhost')
if(conn.is_connected()):
    print("database connected sucessfully")
sql='show databases'# mysql query
myc=conn.cursor()# creating object of cursor class to run execute function
myc.execute(sql)# this will execute mysql query 
for db in myc:
    print(db)

myc.close()
conn.close()
