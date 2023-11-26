from threading import Thread, Event
from time import sleep
def light_switch():
    sleep(3)
    e.set()
    print("green light on")
    sleep(5)
    print("red light on")
    e.clear()
def traffic():
    e.wait()
    while e.is_set():
        print("you can go")
        sleep(.5)
    print("program done")
e=Event()
t1=Thread(target=light_switch)
t2=Thread(target=traffic)
t1.start()
t2.start()

