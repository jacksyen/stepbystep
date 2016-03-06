import socket
import os

HOST ='192.168.0.1'
PORT=5000
BUFFER=4096

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((HOST,PORT))
socket.send('hello,tcp server!')
recv=socket.recv(BUFFER)

print('[tcpServer said]: %s' % recv)

sock.close();





    