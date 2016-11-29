from socket import *
import select

data = None

timeout = 3
msg = "test"
host = "192.168.8.101"
print ("Connecting to " + host)

port = 23

s= socket(AF_INET,SOCK_STREAM)
print "Socket made"

ready = select.select([s],[],[],timeout)
s.connect((host,port))
print("Connection made")

while True :
    if data != None:
        print("sending message")
        s.sendall(msg)
        data = None
        print("message out")
        continue
    if ready[0]:
        data = s.recv(4096)
        print("Data receive")
        print data
        continue
    
