from threading import Thread
from queue import Queue
import time as tt
class producer:
    def __init__(self):
        self.q=Queue()
    def produce(self):
        for i in range(1,6):
            print("item produced",i)
            self.q.put(i)
            tt.sleep(1)

class consumer:
    def __init__(self,prod):
        self.prod=prod
    def consume(self):
        for i in range(1,6):
            print("item recived",self.prod.q.get(i))

p=producer()
c=consumer(p)
t1=Thread(target=p.produce)
t2=Thread(target=c.consume)
t1.start()
t2.start()
