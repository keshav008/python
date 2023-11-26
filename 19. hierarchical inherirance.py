class father:
    def __init__(self):
        print("father class constructor")
    def show(self):
        print("father class method")

class son(father):
    def __init__(self):
        super().__init__()
        print("son class construstor")
    def disp(self):
        print("son class method")

class daughter(father):
    def __init__(self):
        super().__init__()
        print("daughter class constructor")
    def dispD(self):
        print("daughter class method")
d=daughter()
s=son()
