from socket import *
import select

data = None

timeout = 3
msg = "test123"
host = "192.168.8.101"
print ("Connecting to " + host)

port = 23

s= socket(AF_INET,SOCK_STREAM)
print "Socket made"

ready = select.select([s],[],[],timeout)
s.connect((host,port))

print("Connection made")

if ready[0]:
    print("Sending message.")
    s.sendall(msg)
    print("Message out")
    data = s.recv(4096)
    print("Data Received")
    print 'Received : ',repr(data)
