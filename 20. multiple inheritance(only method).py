class father:
    def __init__(self):
        print("father calss constructor")
    def showf(self):
        print("father class method")

class mother:
    def __init__(self):
        print("mother class constructor")
    def showm(self):
        print("mother calss method")

class child(father,mother):
    def __init__(self):
        print("child class constructor")
    def shows(self):
        print("child class method")
c=child()
c.showf()
c.showm()
c.shows()
