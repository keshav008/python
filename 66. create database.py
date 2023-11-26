import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',host='localhost')
if(conn.is_connected()):
    print('connected to mysql sucessfully')
sql='create database python' # mysql query
myc=conn.cursor() # creating object of cursor class
myc.execute(sql) # execute query
myc.close()
conn.close()# close connection
