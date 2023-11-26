class mobile:
    def __init__(self,m):#constructor with formal argument m
        self.model=m
    def show_model(self):
        print('model:',self.model)
realme=mobile('redmi5')
realme.show_model()
