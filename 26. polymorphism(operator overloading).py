class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x+other.a

class B:
    def __init__(self,a):
        self.a=a

a=A(100)
b=B(200)
print(a+b)
 
