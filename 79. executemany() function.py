import mysql.connector
conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
if (conn.is_connected()):
    print("connection established")
else:
    print("somwthing went wrong")
sql='insert into student (name,roll,fee) values (%s,%s,%s)'
myc=conn.cursor()
params=[("shivam",110,40000.5),("vikash",112,35000.2),("nitin",113,25000.6)] # sequence of parameters
try:
    myc.executemany(sql,params)
    conn.commit()
    print("data insreted sucessfully")
except:
    conn.rollback()
    print("unable to insert data")
myc.close()
conn.close()
