from threading import *
from time import sleep
lst=[]
def produce():
    cv.acquire()
    for i in range(1,6):
        lst.append(i)
        sleep(1)
        print("item produced")
    cv.notify()
    cv.release()
def consume():
    cv.acquire()
    cv.wait(timeout=0)
    cv.release()
    print(lst)
    print("your product is ready you can take")
cv=Condition()
t1=Thread(target=produce)
t2=Thread(target=consume)
t1.start()
t2.start()
