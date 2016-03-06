#!/usr/bin/env python 
# -*- coding: UTF-8 -*- 
 
import socket 
 
HOST='192.168.0.100' 
PORT=50001 
BUFFER=4096 
 
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.connect((HOST,PORT)) 
sock.send('hello, udpServer!') 
recv=sock.recv(BUFFER) 
print('[udpServer said]: %s' % recv) 
sock.close()