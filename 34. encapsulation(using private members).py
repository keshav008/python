class rectangle:
    __length=0# private variables
    __breadth=0
    def __init__(self):
        self.__length=10
        self.__breadth=20
        print(self.__length)
        print(self.__breadth)
rec=rectangle()
print(rec.__length)# printing outside the calss
print(rec.__breadth)
