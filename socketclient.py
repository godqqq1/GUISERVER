import socket
#/client

TCP_IP = '192.168.8.100'
TCP_HOST = 3007
BUFFER_SIZE = 12

SERVER_IP = '192.168.8.101'
SERVER_PORT = 80

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((TCP_IP,TCP_HOST))


while True:
    
    data,addr = s.recvfrom(BUFFER_SIZE)
    if not data: break
    print 'received data: ',data
    print 'data receiced from: ',addr
s.close()
