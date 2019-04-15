#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    data  = data.decode(encoding='utf-8')
    
    data = "at %s :%s"%(ctime(),data)
    udpSerSock.sendto(data.encode(encoding='utf-8'),addr)
    print ('...connected from and returned to:', addr)

udpSerSock.close()
