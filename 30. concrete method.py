from abc import ABC, abstractmethod
class father(ABC):
    @abstractmethod
    def show(self):# abstract method
        pass
    def disp(self):
        print("i am concrete method")# concrete method

class son(father):
    def show(self):
        print("abstract method defining")

s=son()
s.disp()
s.show()
