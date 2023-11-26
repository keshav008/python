class father:
    def __init__(self):
        print("father class constructor")
    def showf(self):
        print("father method")

class son(father):
    def __init__(self):
        super().__init__()
        print("son class constructor")
    def shows(self):
        print("son method")

class grandson(son):
    def __init__(self):
        super().__init__()
        print("grandson class construstor")
    def showg(self):
        print("grandson method")
g=grandson() # call both three construstors
