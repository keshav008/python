from threading import Thread
def disp(a,b):
    print("thread running:",a,b)
t=Thread(target=disp, args=(10,20)) # craeting object of thraed class 
t.start()# strating a thraed
