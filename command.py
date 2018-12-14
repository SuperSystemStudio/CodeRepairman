import os
import sys
# main
def main():
    mode=0
    command = input()
    if command == 'su':
        if mode == 0:
            print('Please input password')
        password=input()
        if password == '10000':
            print('welcome')
            mode = 1
        else:
            print('Password error!')
    else:
        print('you are root')
    elif command == 'stop':
        stop()
# stop 
def stop():
    if mode == 0:
        sys.exit()
    elif mode == 1:
        os._exit()
