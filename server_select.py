import socket
import os
import sys
import select


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

readsocks, writesocks = [], []
active_socks = []
active_socks.append(s)

while True:
    readsocks = active_socks.copy()
    print("1\n")
    res = select.select(readsocks, [], [])
    print(type(res))
    print(type(res[0]))
    readables, writeables = res[0:2]
    for sockobj in readables:
        if sockobj == s:
            print("new connection\n")
            new_host = s.accept()
            active_socks.append(new_host[0])
        else:
            data = sockobj.recv(1024)
            if not data:
                sockobj.close()
                readsocks.remove(sockobj)
            else:
                sockobj.send(data)
                sockobj.close()
                active_socks.remove(sockobj)
