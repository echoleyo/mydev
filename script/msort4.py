from time import time
num = 0
def msort4(x):
    global num
    print num
    print "len(x)-> %s" %len(x)
    num+=1
    result = []
    print "x --> %s" %x
    if len(x) < 20:
        return sorted(x)
    mid = int(len(x)/2)
    print "x --> %s" %x
    print "mid = int(len(x)/2) --> %s" %mid
    # y1 = x[:mid]
    # print "y1 = x[:mid] --> %s" %y1
    print "------here"
    y = msort4(x[:mid])
    print "y = msort4(x[:mid]) --> %s" %y
    # z1 = x[mid:]
    # print "z1 = x[mid:] --> %s" %z1
    z = msort4(x[mid:])
    print "z = msort4(x[mid:]) --> %s" %z
    i = 0
    j = 0
    while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
    result += y[i:]
    print "y[i:] -> %s" %y[i:]
    result += z[j:]
    print "z[j:] -> %s" %z[j:]
    return result
    
aList = [15,8,59,69,45,23, 2 ,1,5,6 ,4,45,66,78,32, 30, 29, 28,27,26,25,21,19,18,16,14,15,11]
# aList = [11, 7, 3, 2]
print len(aList)
ts = time()
print msort4(aList)
t2 = time() - ts


ts1 = time()
sorted(aList)

print "msort4 spend: %s" %(t2)
print "sorted spend: %s" %(time() - ts)