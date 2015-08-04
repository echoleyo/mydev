'''
Created on Jul 22, 2015

@author: yali
'''


def oct_to_bin(o):
    OCT = {"0":"000", "1": "001", "2":"010", "3":"011", "4":"100", "5":"101", "6":"110", "7":"111" }
    binstr = ''
    for i in o:
        binstr += OCT[i]
    return binstr


def oct_to_decimal(o):
    for i, v in reversed(enumerate(o)):
        dec = int(v) * 8 ** i
    return dec

if __name__ == '__main__':
    print oct_to_bin("14"), bin(12)
    