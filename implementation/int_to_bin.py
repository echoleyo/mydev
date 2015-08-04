'''
Created on Jul 21, 2015

@author: yali
'''


def int_to_bin(i):
    BIN = "01"
    b = ['0b']
    if 1 == i >= 0:
        return b.insert(1, BIN[i])
    else:
        while i / 2 > 0:
            r = divmod(i, 2)
            if r[0] < 2:
                b.insert(1, BIN[r[1]])
                b.insert(1, BIN[r[0]])
            else:
                b.insert(1, BIN[r[1]])
            i = r[0]
        return "".join(b)


if __name__ == '__main__':
    print int_to_bin(12), bin(12)
    print int_to_bin(112), bin(112)
    print int_to_bin(12234), bin(12234)