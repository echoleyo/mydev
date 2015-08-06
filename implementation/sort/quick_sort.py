'''
Created on Aug 6, 2015

@author: yali
'''


#def quick_sort(arg_list):
#    less = []
#    middle = []
#    more = []
#    if len(arg_list) <= 1:
#        return arg_list
#    else:
#        first = arg_list[0]
##        print "first: %s" % first
#        for i in arg_list:
#            if i < first:
#                less.append(i)
#            elif i > first:
#                more.append(i)
#            else:
#                middle.append(i)
#        less = quick_sort(less)
#        more = quick_sort(more)
#        ll = less + middle + more
#        return ll
##if __name__ == '__main__':
#
##print "sorting ..."
##rev = quick_sort(l)
##print "rev: %s" % rev
##print "finished"
#
#def quickSort(arr):
#    less = []
#    pivotList = []
#    more = []
#    if len(arr) <= 1:
#        return arr
#    else:
#        pivot = arr[0]
#        for i in arr:
#            if i < pivot:
#                less.append(i)
#            elif i > pivot:
#                more.append(i)
#            else:
#                pivotList.append(i)
#        less = quickSort(less)
#
#        more = quickSort(more)
#        return less + pivotList + more
#
#a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
#print "sorting ..."
#aa = quickSort(a)
#print aa

def qsort(list):
    if not list:
        return []
    else:
        first = list[0]
        less = [x for x in list     if x < first]
        more = [x for x in list[1:] if x >= first]
#        print "first: %s" % first
        return qsort(less) + [first] + qsort(more)

if __name__ == '__main__':
    l = [11, 2, 4, 3, 66, 55, 33, 675, 343, 232, 1, 34, 234, 778, 23423]
    print qsort(l)
    print l

