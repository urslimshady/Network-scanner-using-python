#python code to create a port scanner using Socket

from socket import *
import time
start_time = time.time()
if __name__ == '__main__':
    target = input("Enter the host address: ")
    target_IP = gethostbyname(target)
    print("Starting scanning on host:", target)


    #will scan only ports lying between 50 to 500
    for i in range(50, 500):
        #AF_INET(For protocols based on IP addresses using IPv4.)
        #SOCK_STREAM(Needs to be provided when a streaming connection based client or server is needed )
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((target_IP, i))
        if (conn==0):
            print('Port %d: OPEN' % (i,))
        s.close
    
print('Time taken:', time.time() - start_time)


