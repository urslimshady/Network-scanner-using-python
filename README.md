# Network-scanner-using-python

Port scanning can be considered as a monitoring(survellience) tool which is used in order to locate the open ports available on a particular host.

Types of information that can be expected after running the port scanner.
1. Open Ports information
2. Operating System informations
3. Services that are running on host


Here are some of the python code snippet to create a port scanner tool using:
1. Socket
2. ICMP(It is not a port scanner, it is used to send ping to check whether the host is up or not)
3. TCP scan

TCP scan :

To establish a TCP connection, the host must perform a three way handshake.

Step 1: try to initiate a connection that starts with a packet that has the SYN flag set

Step 2: the target system will then respond with a SYN and ACK flag

Step 3: the host will then send ACK packet to target system.
