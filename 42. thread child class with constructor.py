from threading import Thread
class mythread(Thread):
    def __init__(self,a):
        Thread. __init__(self)# calling thread class construstor
        print("child constructor",a)
    def run(self):# this method will wait for execution of one thread completely
        pass
t=mythread(10)
t.start() # strating thread
print("main thread")
