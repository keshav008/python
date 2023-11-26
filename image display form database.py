import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='keshav',host='localhost')
print(conn.is_connected())
sql='select * from image'
myc=conn.cursor()
image=myc.execute(sql)
print(image)
myc.close()
conn.close()
