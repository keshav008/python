from threading import Thread
def disp():
    print("daemon thread")
t1=Thread(target=disp)
print("before",t1.isDaemon())
t1.setDaemon(True)
print("after", t1.isDaemon())
t1.start()
