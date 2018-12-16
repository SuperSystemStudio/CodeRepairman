# import list
import socket
import os
import time
import function_table
function_table.begin()
# Public variable
mode=0
true=1
# main
server = socket.socket() #获得socket实例
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("localhost",22)) #绑定ip port
server.listen()  #开始监听

while True: #第一层loop
    print("等待客户端的连接...")
    conn,addr = server.accept() #接受并建立与客户端的连接,程序在此处开始阻塞,只到有客户端连接进来...
    print("新连接:",addr )
    while True:

        data = conn.recv(1024)
        if not data:
            print("客户端断开了...")
            break #这里断开就会再次回到第一次外层的loop
        print("收到命令:",data)
        if data == b'su':
            if mode == 0:
                mode = 1
                conn.sendall(bytes("now,you are root!",encoding="utf-8"))
            elif mode == 1:
                conn.sendall(bytes("you are already root!",encoding="utf-8"))
        elif data == b'stop':
            if mode == 0:
                sys.exit()
            elif mode == 1:
                os._exit()
        else:
            print(data,':no find the command')
            time.sleep(1)

server.close()
