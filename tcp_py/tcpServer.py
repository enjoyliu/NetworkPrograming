#!/usr/bin/env python

from socket import *
from time import ctime


# host空白表示可以使用任何可用的地址
HOST = ''  
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

#分配tcp服务socket
tcpSerSock = socket(AF_INET, SOCK_STREAM)
#绑定地址
tcpSerSock.bind(ADDR)
#拒绝/转接前传入连接的最大请求数
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        #tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'), data))
        tcpCliSock.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))

    tcpCliSock.close()
tcpSerSock.close()
