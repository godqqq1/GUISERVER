from select import *
import sys
import socket

HOST = '192.168.8.100'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
while 1:
   	conn, addr = s.accept()
	data = conn.recv(1024)
	if data:
	   	print('Connected by ',addr ,' Client : ', data)
	else:
		conn.close()
	try:
		conn.sendall('abc\r')
	except Exception as e:
		conn.close()
		print("Lost Conn")
conn.close()
