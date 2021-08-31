#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 10:56:42 2021

@author: harsh
"""
#1st socket script

import socket 
mysock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org' , 80))     #80 is port number 
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
mysock.close()


#same thing but using urllib 
#skips all the headers
import urllib.request, urllib.error, urllib.parse
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
count = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word,0)+1
print(count)
