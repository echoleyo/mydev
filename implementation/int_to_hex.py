'''
Created on Jul 21, 2015

@author: yali
'''


def int_to_hex(i):
    HEX = '0123456789abcdef' 
    if i <= 15:
        return HEX[i]
    else:
        h = ['0x']
        while (i / 16) > 0:
            r = i / 16
            if r <= 15:
                h.insert(1,  HEX[i%16])
                h.insert( 1, HEX[r])
            else:
                h.insert(1, HEX[i%16])
            i = i / 16
        return "".join(h)


if __name__ == '__main__':
    print int_to_hex(10)
    print int_to_hex(323456)