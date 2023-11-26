import mysql.connector
config={ 'user':'root',
       'password':'Keshav@0001',
       'host':'localhost',
       'port':3306
    }
conn=mysql.connector.connect(**config)
print(conn.is_connected())
