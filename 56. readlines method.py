f=open("student.txt",mode='r')# opening a file in reading mode
data=f.readlines()
f.close()
print(data)
print("program done")
