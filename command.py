import os
import sys
mode=0
# begin
def init():
    name='user'
    print('现在你的用户名为',name)
    main()
# main
def main():
    command = input()
    if command == 'su':
        if mode == 0:
            print('Please input password')
        password=input()
        if password == '10000':
            print('welcome')
            mode = 1
            name = 'root'
        else:
            print('Password error!')
    else:
        print('you are root')
    if command == 'stop':
        stop()
# stop 
def stop():
    if name == 'user':
        sys.exit()
    elif name == 'root':
        os._exit()
