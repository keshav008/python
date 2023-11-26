import mysql.connector
def student_data(nm,rl,fe):
    conn=mysql.connector.connect(user='root',password='Keshav@0001',database='python',host='localhost')
    sql='insert into student(name,roll,fee) values (%(name)s,%(roll)s,%(fee)s)'
    myc=conn.cursor()
    params={'name':nm,'roll':rl,'fee':fe}# dictionary for values
    try:
        myc.execute(sql,params)
        conn.commit()
        print("data inserted")
    except:
        conn.rollback()
        print("unable to insert data")
    myc.close()
    conn.close()

while True:
    nm=input("enter name:")
    rl=int(input("enter roll:"))
    fe=float(input("enter fees:"))
    student_data(nm,rl,fe)
    ans=input("want to exit y/n:")
    if(ans=='y'):
        break
