class duck:
    def walk(self):
        print("duck class method")

class horse:
    def walk(self):
        print("horse calss method")

class cat:
    def talk(self):
        print("cat class method")

def mymethod(obj):
    if(hasattr(obj,'walk')):# this function will check for both 'walk' and 'talk'
        obj.walk()
    if(hasattr(obj,'talk')):
        obj.talk()

d=duck()
mymethod(d)
h=horse()
mymethod(h)
c=cat()
mymethod(c)
