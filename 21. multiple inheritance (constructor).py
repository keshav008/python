class father:
    def __init__(self):
        super().__init__()
        print("father constructor")
    def showf(self):
        print("father method")

class mother:
    def __init__(self):
        super().__init__()
        print("mother constructor")
    def showm(self):
        print("mother method")

class child(father,mother):
    def __init__(self):
        super().__init__()
        print("child construstor")
    def showc(self):
        print("child method")
c=child()
