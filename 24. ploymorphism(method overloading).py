#method overloading is when one more than one method are there in same class
# in python method overloading is not
# in python if one function is performing more than one task ac to the parameters passd
class myclass:
    def sum(self,a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            s=a+b+c
        elif(a!=None and b!=None):
            s=a*b
        elif(b!=None and c!=None):
            s=b-c
        else:
            s=0
        return s
obj=myclass()
print(obj.sum(None,10,20))
