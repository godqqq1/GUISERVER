﻿from socket import *
from select import *
import sys
from time import ctime

who = ["a","b","c"]
HOST = '192.168.8.102'
PORT = 80
BUFSIZE = 1024
ADDR = (HOST, PORT)

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(ADDR)

serverSocket.listen(10)
connection_list = [serverSocket]
print('==============================================')
print('Server Start. Port : %s ' % str(PORT))
print('==============================================')

while connection_list:
    try:
        print('[INFO] Wait...')

        read_socket, write_socket, error_socket = select(connection_list, [], [], 10)

        for sock in read_socket:
            if sock == serverSocket:
                clientSocket, addr_info = serverSocket.accept()
                connection_list.append(clientSocket)
                print('[INFO][%s] Client (%s) is Connected.' % (ctime(), addr_info[0]))

                for socket_in_list in connection_list:
                    if socket_in_list != serverSocket and socket_in_list != sock:
                        try:
                            socket_in_list.send('[%s] New Client come. Hello!' % ctime())
                        except Exception as e:
                            socket_in_list.close()
                            connection_list.remove(socket_in_list)
            else:
                data = sock.recv(BUFSIZE)
                if data:
                    print('[INFO][%s] Client send Message %s' % (ctime(),data))
                    for socket_in_list in connection_list:
                        if socket_in_list != serverSocket and socket_in_list != sock:
                            try:
                                socket_in_list.send('123')
                                print('[INFO][%s] Send Message.' % ctime())
                            except Exception as e:
                                print(e.message)
                                socket_in_list.close()
                                connection_list.remove(socket_in_list)
                                continue
                else:
                    connection_list.remove(sock)
                    sock.close()
                    print('[INFO][%s] Black out' % ctime())
    except KeyboardInterrupt:
        serverSocket.close()
        sys.exit()
