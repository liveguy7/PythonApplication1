import time

#get the time of a program's execution

def methodmodule3(a):
    start_time = time.time()
    s = 0
    for i in range(0,a+1,1):
        s = s + i
    end_time = time.time()
    return s, end_time-start_time


