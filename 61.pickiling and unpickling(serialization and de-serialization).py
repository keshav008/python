import pickle

class student:
    def __init__(self,name,roll,address):
        self.name=name
        self.roll=roll
        self.address=address
    def disp(self):
        print(f'Name:{self.name} Rollno:{self.roll} Address{self.address}')

with open('student.dat',mode='wb') as f:
    stu1=student("prashant",1001,'moradabad')
    stu2=student("keshav",1002,'amroha')
    pickle.dump(stu1,f)# this function return the pickled representation of thge object
    pickle.dump(stu2,f)
    print("pickling done")
    stu1.disp()
    stu2.disp()

with open('student.dat',mode='rb')as f:
    obj1=pickle.load(f)# this function read pickled object and retrun it into object
    obj2=pickle.load(f)
    print("unpickling done")
    print(f.read())# this function is unable to read the data from file
    obj1.disp()
    obj2.disp()
