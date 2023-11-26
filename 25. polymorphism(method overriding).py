
#class father:
 #   def add(self,a,b):
  #      print("addition value",a+b)

#class son(father):
#    pass
#c=son()
#c.add(10,20)

class father:
    def multi(self,x,y):
        print("additon",x+y)

class son(father):
    def multi(self,a,b):
        super().multi(10,20) # call parent calss multi method
        print("multiplication",a*b)

s=son()
s.multi(10,20)# call both parent and child calss methods
