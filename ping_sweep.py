#python code snippet to ping a system to get opened ports by sending ICMP packets.
#author @Rohit
import os
import platform

from datetime import datetime
net = input("Enter the network address: ")
net1 = net.split('.')
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input("Enter the starting number: "))
en1 = int(input("Enter the last number: "))
en1 = en1 + 1
operation = platform.system()

if(operation == "Windows"):
    ping1 = "ping -n 1 "
elif(operation == "Linux" ):
    ping1 = "ping -c 1 "
else:
    ping1 = "ping -c 1 "
t1 = datetime.now()
print("Scanning in progress...")

for ip in range(st1, en1):
    address = net2 + str(ip)
    command = ping1 + address
    response = os.popen(command)

    for line in response.readlines():
        if(line.count("TTL")):
            break
        if(line.count("TTL")):
            print(address, "-->live")

t2 = datetime.now()
total = t2 -t1
print("Scanning completed in: ", total)

