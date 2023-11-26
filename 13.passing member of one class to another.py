class student:
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    def disp(self):
        print("name:",self.name)
        print("roll no:",self.roll)

class user:
    #@staticmethod # optional
    def show(self):
        print("username:",self.name)
        print("rollnumber:",self.roll)

stu=student('rahul',101)
user.show(stu) #passing object of first class in the function calling of second class
