'''
Created on Jul 30, 2015

@author: yali
'''
def msort2(x):
    if len(x) < 2:
        return x
    result = []  # moved!
    mid = int(len(x) / 2)
    y = msort2(x[:mid])
    print "left (y): %s" % y
    z = msort2(x[mid:])
    print "right (z): %s" % z
    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:
                print "add z[0]", z[0]
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
    result += y
    result += z
    print "y: %s" % y
    print "z: %s" % z
    return result

l = [212, 3, 45, 654, 3, 534, 22, 33, 4, 2, 2, 1, 7]
#l = [122, 5]
print "start"
#print msort2(l)

def bubble_sort(items):
    """ Implementation of bubble sort """
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items
print bubble_sort(l)
