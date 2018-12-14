import os
import sys
import time
import function_table
platform = function_table.platform
# main
def main():
    mode=0
    true=1
    while true == 1:
        print('Please enter the command')
        command = input()
        if command == 'su':
            if mode == 0:
                print('Please input password')
                password=input()
                if password == '10000':
                    print('welcome')
                    mode = 1
                    print('now,you are root')
            elif mode == 1:
                print('you are root')
            else:
                print('Password error!')
        elif command == 'stop':
            if mode == 0:
                sys.exit()
            elif mode == 1:
                os._exit()
        else:
            print(command,':no find the command')
            time.sleep(1)