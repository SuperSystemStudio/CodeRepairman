# import list
import socket
import os
import time
import function_table
import random
import threading
import sys
function_table.begin
# Public variable
platform = sys.platform
# main
def sshserver():
    server = socket.socket() #获得socket实例
    #server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if platform == 'liunx':
        port = 8888
    else:
        port = 22
    server.bind(("localhost",port)) #绑定ip port
    print('ssh is running at 127.0.0.1:22')
    server.listen()  #开始监听
    mode=0
    while True: #第一层loop
        print("Waiting for client connection")
        conn,addr = server.accept() #接受并建立与客户端的连接,程序在此处开始阻塞,只到有客户端连接进来...
        print("[new user]>>>",addr )
        while True:
            data = conn.recv(1024)
            if not data:
                print("client is disconnected")
                break #这里断开就会再次回到第一次外层的loop
                print("收到命令:",data)
            if data == b'su':
                if mode == 0:
                    mode = 1
                    conn.sendall(bytes("now,you are root!",encoding="utf-8"))
                elif mode == 1:
                    conn.sendall(bytes("you are already root!",encoding="utf-8"))
            elif data == b'stop':
                os._exit(0)
                function_table.close()
                c = random.randint(1,2)
                if c == 1:
                    conn.sendall(bytes("see you again!",encoding="utf-8"))
                elif c == 2:
                    conn.sendall(bytes('goodbye!',encoding="utf-8"))
            else:
                print('Error: no find the command')
                conn.sendall(bytes('Error: no find the command',encoding="utf-8"))
                time.sleep(1)

    server.close()
def main():
    pass
try:
    ssh=threading.Thread(target=sshserver)#创建线程
    main=threading.Thread(target=main)
    # true为后台运行，false为前台运行
    main.setDaemon(False)
    ssh.setDaemon(True)
    main.start()
    ssh.start()
    ssh.join(10)
    main.join()
except:
   print ("Error: Unable to start threads")
   os._exit(0)
