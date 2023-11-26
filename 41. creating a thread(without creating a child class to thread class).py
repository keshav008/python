from threading import Thread
class mythread:
    def disp(self,a,b):
        print(a,b)
myt=mythread()
t=Thread(target=myt.disp, args=(10,20))
t.start()
