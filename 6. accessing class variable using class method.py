class mobile:
    name="keshav"# class variable
    def __init__(self):# constustor
        self.model='redmi'# instance variable
    def show_model(self):# instance method
        print(self.model)# accessing instace variable
    @ classmethod # decorator
    def my_name(cls):# class method
        print(cls.name)#accessing class varibale
obj=mobile()
obj.my_name()
