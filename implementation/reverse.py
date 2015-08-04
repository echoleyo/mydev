'''
Created on Jul 13, 2015

@author: yali
'''

def r(s):
    return s[::-1]


def reverse_string(strs):
    new_str = []
    for i in (i for i in str):
        new_str.insert(0, i)
    return ''.join(new_str)


def reverse_str(strs):
    new_str = []
    count = len(str) - 1
    while count >= 0:
        new_str.append(str[count])
        count -= 1
    return ''.join(new_str)


if __name__ == '__main__':
    print reverse_str("hello")