'''
Created on Jul 21, 2015

@author: yali
'''


def int_to_oct(i):
    OCT = "01234567"
    o = ['0']
    if i <= 7:
        return OCT[i]
    else:
        while i / 8 > 0:
            r = i / 8
            if r < 7:
                o.insert(1, OCT[i%8])
                o.insert(1, OCT[r])
            else:
                o.insert(1, OCT[i%8])
            i = i / 8
        return "".join(o)


if __name__ == '__main__':
    print int_to_oct(12)
    print int_to_oct(112)
    print int_to_oct(12234)