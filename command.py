import os
import sys
# begin
def begin():
    name = 'user'
# main
def main():
    begin()
    command = input()
    if command == 'su':
        Login() 
    if command == 'stop':
        stop()
# root
def Login():
    if name == 'user':
        print('Please input password')
        password=input()
        if password == '10000':
            print('welcome')
            name = 'root'
        else:
            print('Password error!')
    else:
        print('you are root')
# stop 
def stop():
    if name == 'user':
        sys.exit()
    elif name == 'root':
        os._exit()
main()
