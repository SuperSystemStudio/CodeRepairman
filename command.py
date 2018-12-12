import os
import sys
name = 1
# main
def main():
    command = input()
    if command == 'su':
        Login() 
    if command == 'stop':
        stop()
# root
def Login():
    if name == 1:
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
    if name == '1':
        sys.exit()
    elif name == 'root':
        os._exit()
main()
