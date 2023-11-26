from threading import *
import time
class flight:
    def __init__(self,available_seat):
        self.available_seat=available_seat
        self.l=BoundedSemaphore(2)
        print(self.l)

    def reserve(self,need_seat):
        self.l.acquire()
        self.l.acquire()
        print(self.l)
        print("available seats:",self.available_seat)
        if(self.available_seat>=need_seat):
            name=current_thread().name
            print(f'{need_seat} is alloted for {name}')
            self.available_seat-=need_seat
        else:
            print("all seats are alloted")
        self.l.release()
        self.l.release()
f=flight(2)
t1=Thread(target=f.reserve, args=(1,),name="keshav")
t2=Thread(target=f.reserve, args=(1,),name="prashant")
t3=Thread(target=f.reserve, args=(1,),name="harman")
t1.start()
t2.start()
t3.start()
print("main thread")
