from time import time,ctime,localtime
epoch=time()
print(epoch)
current_time=ctime(epoch)# give current time
print("current time",current_time)
local_time=localtime()# give local time
print("local time",local_time)
