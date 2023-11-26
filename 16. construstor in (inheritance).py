class father:
    def __init__(self):
        self.money=1000
    def show(self):
        print("instance method of parent class")
        print(self.money)
        
class child(father):
    def __init__(self):
        self.money=5000 # this value is updated by child calss constructor
        self.name="keshav"
    def disp(self):
        print("instance method of child class")
        print(self.money,self.name)
c=child()
f=father()
c.show()
c.disp()
f.show()
