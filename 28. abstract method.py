from abc import ABC, abstractmethod
class father(ABC):
    @ abstractmethod
    def sides(self):# abstract method
        pass
class triangle(father):
    def sides(self): # overriding abstact method
        print("i have three sides")
class square(father):
    def sides(self):
        print("i have four sides")

t=triangle()
t.sides()
s=square()
s.sides()
