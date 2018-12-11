import random
import sys
import test
# Public variable
platform = sys.platform
# begin
def begin() :
    c = random.randint(1,2)
    if c == 1:
        print('hello world')
    elif c == 2:
        print('hi')
# close
def close():
    c = random.randint(1,2)
    if c == 1:
        print('goodbye!')
    elif c == 2:
        print('see you again!')
# test
test.platform()