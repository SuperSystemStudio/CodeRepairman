import random
import sys
# Public variable
platform = sys.platform
# begin
def begin() :
    c = random.randint(1,2)
    if c == 1:
        print('hello world')
    elif c == 2:
        print('hi')
def close():
    c = random.randint(1,2)
    if c == 1:
        print('goodbye!')
    elif c == 2:
        print('see you again!')
