class shape:
    _length=10 # protected members
    _breadth=20
class circle(shape):
    def __init__(self):
        print(self._length)
        print(self._breadth)
cr=circle()
print(cr.length)# printing outside the derived class 
print(cr.breadth)
