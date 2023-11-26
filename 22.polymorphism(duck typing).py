class duck:
    def walk(self):
        print("duck calss method")

class horse:
    def walk(self):
        print("horse class method")

class cat:
    def talk(self):
        print("cat class method")

def myfunction(obj):
    obj.walk()# this will call only walk meyhod of each class not talk method

d=duck()# creating object of duck class
myfunction(d)# function calling with duck class object
h=horse()# creting object of horse calss
myfunction(h)# calling method with horse calss object
c=cat()# creating object of cat class 
myfunction(c)# calling method with cat class
