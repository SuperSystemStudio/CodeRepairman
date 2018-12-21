import sys
def platform():
    platform = sys.platform
    if platform == 'win32':
        print('This is windows')
    if platform == 'liunx':
        print('this is liunx')
    print(platform)