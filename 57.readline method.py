f=open("student.txt",mode='r')# opening a file in reading mode
data=f.readline()
print(f.tell())# this function will find the current position of pointer
f.seek(1)# this method will move pointer to one location to other
print(f.tell())
f.close()
print(data)
print("program done")
