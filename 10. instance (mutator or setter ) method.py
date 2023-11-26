#class mobile:
 #   def __init__(self, company):
  #      self.model=company
   # def set_model(self, company):
    #    self.model=company
#realme=mobile('realme')# original value for self.model
#realme.set_model('redmi')# modified value for self.model
#print(realme.set_model('redmi'))

class Car:
    def __init__(self, carMake):
        self.__make = carMake

    #Mutator Methods
    def set_make(self, carMake):
        self.__make = carMake

    #Accessor Methods
    def get_make(self):
        return self.__make


myCar=Car('Ford',)
myCar2=Car('Nissan')
print(myCar.get_make())
print(myCar.set_make('Porche'))
print(myCar.get_make())

