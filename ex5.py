import os
import time
from threading import Thread
def pingcheck(counter,ip):
    counter+=1
    print ("In thread no "+str(counter)+" pinging "+ip) 
    response=os.system("ping -c 1 " + ip)
    if response==0: print(ip,"is active")
    else: print (ip,"is inactive")
    print ("Sleeping for 5 secs")
    time.sleep(5)
    print('slept')
    return

iplist=[]
counter=0
print ("Enter the list of IPs you want to ping ")
while True:
    d=input()
    if d=="end": break
    iplist.append(d)
for ip in iplist:
    t= Thread(target=pingcheck, args=(counter,ip,))
    t.start()
