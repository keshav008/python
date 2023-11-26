class father:
    def __init__(self):
        self.money=1000
        self.name="keshav"
    def show(self):
        print("parent class instance method")
        print(self.money)
        print(self.name)

class child(father):
    def __init__(self):
        self.name="tripti"
        super().__init__() # this will called parent class constructor only
    def disp(self):
        print("child class instance method")
        print(self.money)
        print(self.name)
c=child()
f=father()
c.disp()
c.show()
f.show()
