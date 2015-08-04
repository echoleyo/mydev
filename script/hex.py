

def HexToBin(x):
    d = {"a":10, "b":11,"c":12,"d":13,"e":14,"f":15}
    l = map(str.lower, list(x[2:]))
    i = 0

    num = 1
    for x in enumerate(l):
        print "l -> %s" %list(enumerate(l))
        print "x -> %s, %s" %(x[0], x[1])
        print "num: %s" %num
        num += 1
        print "if x in d: --> %s" % (x in d)
        if x[1] in d:
            print "In d x[1] -> '%s'" %x[1]
            i += 16**(len(l)-1)*d[x[1]]
            print "16**(len(l)-1)*int(d[x]) ->%s" %i
            l.remove(x[1])
            print "In d l.remove(x) --> %s" %l
        else:
            print i
            print "NOT In d x[1] -> '%s'" %x[1]
            i += 16**(len(l)-1)*int(x[1])
            print "16**len(l)*int(x) -> %s" %i
            l.remove(x[1])
            print "not in d l.remove(x) --> %s" %l
    
    return i
    
h = '0x11A'
"1*16*16+1*16 + 10"
print HexToBin(h)
print "It should be: %s " %int(h, 16)

