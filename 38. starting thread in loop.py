from threading import Thread
def disp():
    print("child thread")
    for i in range(5):
        print("child thread")
t=Thread(target=disp)
t.start()
print()
for i in range(5):
    print("main thread")
