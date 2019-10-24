import socket
import os
import sys
import select


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

readsocks, writesocks = [], []
active_socks =[]

while True:
    readsocks = active_socks.copy()
    readables, writeables = select.select(readsocks, writesocks, [])
    for sockobj in readables:
        if sockobj == s:
            new_host, new_port = s.accept()
            active_socks.append((new_host, new_port))
        else:
            data = sockobj.recv(1024)
            if not data:
                sockobj.close()
                readsocks.remove(sockobj)
            else:
                sockobj.send(data)
                sockobj.close()
                active_socks.remove(sockobj)



        
