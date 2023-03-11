from threading import *
import time
def cal(p):
    for i in p:
        time.sleep(1)
        print(i**i)

def squ(p):
    for i in p:
        time.sleep(1)
        print(i*i)

p=list(range(10))
t1=Thread(target=cal,args=(p,))
t2=Thread(target=squ,args=(p,))

starttime= time.time()
t1.start()
t2.start()
t1.join()
t2.join()
endtime= time.time()
totaltime= endtime-starttime
print(totaltime)

