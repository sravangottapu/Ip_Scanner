import threading
import time
import os
import re
import shlex
import _thread
import sys
import subprocess
alive = True
f = open("list.txt","w")
class myThread(threading.Thread):
    def __init__(self,var,ip):
        threading.Thread.__init__(self)
        self.var = var
        self.ip = ip
    def run(self):
        if(alive):
            ping_ip(self.var,self.ip)
            #self._stop.set()
            print("Thread Exited")
def ping_ip(cmd,ip):
    try:
        output = subprocess.check_output(cmd)
        f.write(ip)
        f.write("\n")
        print(ip + "Reachable")
    except:
        print(ip + "Not Reachable")
first = input("Enter the first Ip")
second = input("Enter the second Ip")
first = int(first)
second = int(second)
ping = "ping "
c1 = "-c1 "
start = time.time()
cmd_no_ip = ping + c1
t_end = time.time() + 2
for i in range(first,second):
    ip = "172.16.114."+str(i)
    cmd = cmd_no_ip + ip
    cmd = shlex.split(cmd)
    try:
        thread1 = myThread(cmd,ip)
        thread1.start()
        thread1.join(1)
    except:
        print("Not thread" + ip)
end = time.time()
end = end - start
alive = False
print("Total Time" + str(end))
sys.exit()
quit()
