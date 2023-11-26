from threading import *
class flight:
    def __init__(self, available_seat):
        self.available_seat=available_seat
        self.l=Lock()
    def reserve(self,need_seat):
        self.l.acquire(blocking=True,timeout=-1)
        print("available seats=",self.available_seat)
        if(self.available_seat>=need_seat):
            name=current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat-=need_seat
        else:
            print("no seat is avialbale")
        self.l.release()

f=flight(2)
t1=Thread(target=f.reserve, args=(1,),name="keshav")
t2=Thread(target=f.reserve, args=(1,),name="tripti")
t3=Thread(target=f.reserve, args=(1,),name="prashant")
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("main thraed")
