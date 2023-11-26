class army:
    def __init__(self):
        self.name="rahul"

    def show(self):
        print(self.name)

# inner class
    class gun:
        def __init__(self):
            self.name='AK47'
            self.round='75 round'
        def disp(self):
            print(self.name,self.round)

    # inner class 2
        class country:
            def __init__(self):
                self.name='india'
            def show_country(self):
                print(self.name)
        con=country()
    gn=gun()
ar=army()
print(ar.name)
print(ar.gn.name)
print(ar.gn.con.name)
#gn.disp()# cannot work in outer class
ar.gn.disp()
ar.gn.con.show_country()
