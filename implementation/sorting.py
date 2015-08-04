'''
Created on Jul 30, 2015

@author: yali
'''


def insertion_sort(items):
    """ Implementation of insertion sort """
    for j in range(1, len(items)):
        print ">>j", j
#         j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            print "j -> ", j
            j -= 1
            print j
    return items

if __name__ == '__main__':
    l = [100, 2,33,4,55,6,77,44,32,12,45,67]
    print insertion_sort(l)