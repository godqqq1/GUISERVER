import socket

HOST = '192.168.8.102'
PORT = 81
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
print 'asd'
s.sendall('Hello,world')
data = s.recv(1024)
s.close()
print 'Received',Repr(data)
