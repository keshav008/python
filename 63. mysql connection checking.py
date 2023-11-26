import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',host='localhost',database='keshav')
print(conn.is_connected()) # this function will tell whether your connection is sucessfully established or not
