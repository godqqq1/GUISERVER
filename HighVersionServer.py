from select import *
import sys
import socket

HOST = '192.168.8.200'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
timer = 10
while 1:
	print(timer)
   	conn, addr = s.accept()
	data = conn.recv(1024)
	if data:
	   	print('Connected by ',addr ,' Client : ', data)
	else:
		conn.close()
	try:
		if(timer == 0) :
			conn.sendall('kill\r')
		else :
			timer = timer - 1
			conn.sendall('abc\r')
	except Exception as e:
		conn.close()
		print("Lost Conn")
conn.close()
