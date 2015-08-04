'''
Created on Jul 21, 2015

@author: yali
'''


def bin_to_decimal(b):
    if b.startswith("0b"):
        b = b[2:]
    d = 0
    for i, v in enumerate(reversed(b)):
        d += int(v) * 2**i
    return d


def bin_to_oct(b):
    "110011101011"
    if b.startswith("0b"):
        b = b[2:]
        o = []
        oc = []
    end = len(b)
    while end > 0:
        start = end - 3
        if start < 0: start = 0
        o.append(b[start:end])
        end = start
    for bb in o:
        v = 0
        for i, x in enumerate(reversed(bb)):
            v += int(x) * 2 ** i
        oc.insert(0, str(v))
    return "".join(oc)
 
 
def bin_to_hex(b):
    HEX = "0123456789abcdef"
    if b.startswith("0b"):
        b = b[2:]
        o = []
        oc = []
    end = len(b)
    while end > 0:
        start = end - 4
        if start < 0: start = 0
        o.append(b[start:end])
        end = start
    for bb in o:
        v = 0
        for i, x in enumerate(reversed(bb)):
            v += int(x) * 2 ** i
        oc.insert(0, str(HEX[v]))
    return "".join(oc)
 

if __name__ == '__main__':
#     print bin_to_decimal("0b1110110"), int( "0b111011", 2)
#     print bin_to_decimal("0b10011011"), int( "0b10011011", 2)
#     print bin_to_decimal("0b111011011"), int( "0b111011011", 2)

    print bin_to_oct("0b1101110"), oct(int("0b1101110", 2))
    print bin_to_oct("0b10011011"), oct(int( "0b10011011", 2))
    print bin_to_oct("0b111011011"), oct(int( "0b111011011", 2))

    print bin_to_hex("0b1101110"), hex(int("0b1101110", 2))
    print bin_to_hex("0b10011011"), hex(int( "0b10011011", 2))
    print bin_to_hex("0b111011011"), hex(int( "0b111011011", 2))