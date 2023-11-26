class father:
    money=1000
    def show(self):
        print("parent class instance method")
    @classmethod
    def show_money(cls):
        print("parent class classmethod")
        print("money:",cls.money)
    @staticmethod
    def view():
        print("parent class static method")
class son(father): # here father is the parent classs
    def disp(self):
        print("child class instance method")
        print(father.money)
f=father()
s=son()
s.show()
s.show_money()
s.view()
s.disp()
f.disp()# parent calss object cant access child calss method
