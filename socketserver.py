# import list
import socket
import os
import time
# Public variable
mode=0
true=1
# main
server = socket.socket() #获得socket实例
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("localhost",9998)) #绑定ip port
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
                print('Please input password')
                password = conn.recv(1024)
                mode = 1
                print('now,you are root')
            elif mode == 1:
                print('you are root')
            else:
                print('Password error!')
        elif data == b'stop':
            if mode == 0:
                sys.exit()
            elif mode == 1:
                os._exit()
        else:
            print(data,':no find the command')
            time.sleep(1)

server.close()