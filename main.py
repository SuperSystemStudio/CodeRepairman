# import list
import socket
import os
import time
import function_table
import random
import threading
function_table.begin
# Public variable

# main
def ssh():
    server = socket.socket() #获得socket实例
    #server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(("localhost",22)) #绑定ip port
    server.listen()  #开始监听
    mode=0
    while True: #第一层loop
        print("等待客户端的连接...")
        conn,addr = server.accept() #接受并建立与客户端的连接,程序在此处开始阻塞,只到有客户端连接进来...
        print("[new user]>>>",addr )
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
                os._exit(0)
                function_table.close()
                c = random.randint(1,2)
                if c == 1:
                    conn.sendall(bytes("see you again!",encoding="utf-8"))
                elif c == 2:
                    conn.sendall(bytes('goodbye!',encoding="utf-8"))
            else:
                print(data,':no find the command')
                conn.sendall(bytes('no find the command',encoding="utf-8"))
                time.sleep(1)

    server.close()
try:
    ssh=threading.Thread(target=ssh)#创建线程
    ssh.setDaemon(True)
    ssh.start()
    ssh.join()
except:
   print ("Error: 无法启动线程")
   os._exit(0)
