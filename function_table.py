import random
import sys
# begin
def begin() :
    c = random.randint(1,2)
    if c == 1:
        print('hello world')
    elif c == 2:
        print('hi')
# Get system information
def os():
    h = sys.platform