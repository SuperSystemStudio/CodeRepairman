import socket   #socket模块
def begin():
    host='127.0.0.1'
    port=50007
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP
    s.bind((host,port))   #套接字绑定的IP与端口
    s.listen(1)         #开始TCP监听,监听1个请求
    while 1:
        conn,addr=s.accept()   #接受TCP连接，并返回新的套接字与IP地址
        print('Connectedby',addr)    #输出客户端的IP地址
        while 1:
            data=conn.recv(1024)    #把接收的数据实例化