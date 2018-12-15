import socket

obj = socket.socket()
obj.connect(("127.0.0.1",8080))

ret = str(obj.recv(1024),encoding="utf-8")
print(ret)