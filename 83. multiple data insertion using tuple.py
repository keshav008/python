import mysql.connector
def student_data(nm,rl,fe):
    conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
    sql='insert into student(name,roll,fee) values (%s,%s,%s)'
    myc=conn.cursor()
    params=(nm,rl,fe)
    try:
        myc.execute(sql,params)
        conn.commit()
        print("data inserted")
    except:
        conn.rollback()
        print("unbale to insert data")
while True:
    nm=input("enter name:")
    rl=int(input("enter roll:"))
    fe=float(input("enter fee:"))
    student_data(nm,rl,fe)
    ans=input("want to exit(y/n)")
    if(ans=='y'):
        break
