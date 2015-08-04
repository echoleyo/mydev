'''
Created on Jul 21, 2015

@author: yali
'''


def enumerated(l):
    start = 0
    for i in l:
        yield start, i
        start += 1

if __name__ == '__main__':
    for i in enumerated("hello world"):
        print i