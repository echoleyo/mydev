'''
Created on Jul 30, 2015

@author: yali
'''


def binary_search(l, item):
    left = 0
    right = len(l) - 1
    found = False

    while right >= left and not found:
        mid = (right + left) // 2
        print "mid num is: %s" % mid
        if item == l[mid]:
            found = True
        elif item > l[mid]:
            print item
            print l[mid]
            print "item in right side"
            left = mid + 1
        else:
            right = mid - 1
        print "left %s" % left
        print "right %s" % right
    return found

ll = [1, 2, 3, 4, 6, 7, 9, 11, 13, 45, 56, 77, 88, 99]
print binary_search(ll, 4)


def binarySearch(alist, item):
        first = 0
        last = len(alist) - 1
        found = False

        while first <= last and not found:
            midpoint = (first + last) // 2
            print "midpoint num is: %s" % midpoint
            if alist[midpoint] == item:
                found = True
            else:
                if item < alist[midpoint]:
                    print "item in left side"
                    last = midpoint - 1
                else:
                    print "item in right side"
                    first = midpoint + 1
                print first
                print last

        return found

#testlist = [0, 1, 2, 3, 4, 5, 8, 13, 17, 19, 32, 42, ]
testlist = [1, 2, 3, 4, 6, 7, 9, 11, 13, 45, 56, 77, 88, 99]
#print(binarySearch(testlist, 4))
#print(binarySearch(testlist, 13))
