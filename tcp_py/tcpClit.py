#!/usr/bin/env python

from socket import *
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--host',metavar='', default='35.201.215.176',dest="host")

parser.add_argument('--port',metavar='', default='21567',type = int, dest="port")

args = parser.parse_args()

HOST = args.host
PORT = args.port
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()
