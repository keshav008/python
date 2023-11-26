from threading import Thread
class mythread(Thread):
    def run(self):
        for i in range(5):
            print("child thread")
t=mythread()
t.start()
t.join()
for i in range(5):
    print("main thread")
