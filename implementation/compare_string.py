'''
Created on Jul 20, 2015

@author: yali
'''


def compare_string(str1, str2):
    ord1 = "".join([str(ord(i)) for i in str1])
    ord2 = "".join([str(ord(i)) for i in str2])
    print ord1
    print ord2
    if int(ord1) == int(ord2):
        return 0
    elif int(ord1) > int(ord2):
        return 1
    else:
        return -1

if __name__ == '__main__':
    print compare_string("hello", "hello")